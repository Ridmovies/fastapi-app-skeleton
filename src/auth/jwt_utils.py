from datetime import timedelta, timezone, datetime
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBearer
from jwt import InvalidTokenError, ExpiredSignatureError

from src.auth.exceptions import credentials_exception, auth_exp
from src.auth.schemas import TokenSchema
from src.auth.service import AuthService
from src.auth.pwd_utils import verify_password
from src.config import settings
from src.users.models import User
from src.users.schemas import UserSchema

http_bearer = HTTPBearer(auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

### JWT HS256
# SECRET_KEY: str = settings.SECRET_KEY
# ALGORITHM: str = settings.ALGORITHM
# PUBLIC_KEY: str = settings.SECRET_KEY

### JWT RS256
SECRET_KEY: str = settings.auth_jwt.private_key_path.read_text()
PUBLIC_KEY: str = settings.auth_jwt.public_key_path.read_text()
ALGORITHM: str = settings.auth_jwt.algorithm

TOKEN_TYPE_FIELD = "type"
ACCESS_TOKEN_TYPE = "access"
REFRESH_TOKEN_TYPE = "refresh"

ACCESS_TOKEN_EXPIRE_MINUTES: int = 15


def encode_jwt(
    payload: dict,
    private_key: str = SECRET_KEY,
    algorithm: str = ALGORITHM,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now = datetime.now()
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        # iat=now,
        # jti=str(uuid.uuid4()),
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = PUBLIC_KEY,
    algorithm: str = ALGORITHM,
) -> dict:
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithm],
        # options={"verify_iat": False},
    )
    return decoded



def create_jwt_token(
    token_type: str,
    token_data: dict,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:
    jwt_payload = {TOKEN_TYPE_FIELD: token_type}
    jwt_payload.update(token_data)
    return encode_jwt(
        payload=jwt_payload,
        expire_minutes=expire_minutes,
        expire_timedelta=expire_timedelta,
    )


def create_access_token(user: UserSchema) -> str:
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
    }
    return create_jwt_token(
        token_type=ACCESS_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_minutes=settings.auth_jwt.access_token_expire_minutes,
    )


def create_refresh_token(user: UserSchema) -> str:
    jwt_payload = {
        "sub": user.username,
    }
    return create_jwt_token(
        token_type=REFRESH_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_timedelta=timedelta(days=settings.auth_jwt.refresh_token_expire_days),
    )


# def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now(timezone.utc) + expires_delta
#     else:
#         expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    expire: int = payload.get("exp")
    if expire < datetime.now(timezone.utc).timestamp():
        raise ExpiredSignatureError
    user = await AuthService.get_user_by_username(username)
    if user is None:
        raise credentials_exception
    return user


# async def get_access_token(form_data: OAuth2PasswordRequestForm) -> TokenSchema | None:
#     username = form_data.username
#     user = await AuthService.get_user_by_username(username)
#     data_dict = {"sub": username}
#     access_token = create_access_token(data_dict)
#     if user is None:
#         raise auth_exp
#     if not verify_password(form_data.password, user.hashed_password):
#         raise auth_exp
#     return TokenSchema(access_token=access_token)


async def validate_auth_user(
    username: str = Form(),
    password: str = Form(),
) -> User | None:
    user = await AuthService.get_user_by_username(username)
    if user is None:
        raise auth_exp
    if not verify_password(password, user.hashed_password):
        raise auth_exp
    return user



def validate_token_type(
    payload: dict,
    token_type: str,
) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"invalid token type {current_token_type!r} expected {token_type!r}",
    )

async def get_user_by_token_sub(payload: dict) -> User:
    username: str | None = payload.get("sub")
    user = await AuthService.get_user_by_username(username)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )


def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
):
    try:
        payload = decode_jwt(token)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token error: {e}",
        )
    return payload


async def get_current_auth_user(
    payload: dict = Depends(get_current_token_payload),
) -> User:
    validate_token_type(payload, ACCESS_TOKEN_TYPE)
    return await get_user_by_token_sub(payload)


async def get_current_user_for_refresh(
    payload: dict = Depends(get_current_token_payload),
) -> User:
    validate_token_type(payload, REFRESH_TOKEN_TYPE)
    return await get_user_by_token_sub(payload)
