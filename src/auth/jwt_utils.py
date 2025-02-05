from datetime import timedelta, timezone, datetime
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import InvalidTokenError
from starlette import status

from src.auth.schemas import TokenSchema
from src.auth.service import AuthService
from src.auth.pwd_utils import verify_password
from src.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

### JWT HS256
# SECRET_KEY: str = settings.SECRET_KEY
# ALGORITHM: str = settings.ALGORITHM
# PUBLIC_KEY: str = settings.SECRET_KEY

### JWT RS256
SECRET_KEY: str = settings.auth_jwt.private_key_path.read_text()
PUBLIC_KEY: str = settings.auth_jwt.public_key_path.read_text()
ALGORITHM: str = settings.auth_jwt.algorithm


ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# def get_current_token_payload(
#     token: str | bytes,
# ):
#     try:
#         payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM])
#     except InvalidTokenError as e:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail=f"Invalid token error: {e}",
#         )
#     return payload


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user = await AuthService.get_user_by_username(username)
    if user is None:
        raise credentials_exception
    return user


async def get_access_token(form_data: OAuth2PasswordRequestForm) -> TokenSchema | None:
    auth_exp = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )
    username = form_data.username
    user = await AuthService.get_user_by_username(username)
    data_dict = {"sub": username}
    access_token = create_access_token(data_dict)

    if user is None:
        raise auth_exp
    if not verify_password(form_data.password, user.hashed_password):
        raise auth_exp
    return TokenSchema(access_token=access_token, token_type="bearer")




