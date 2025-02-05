from datetime import timedelta, timezone, datetime
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import InvalidTokenError, ExpiredSignatureError

from src.auth.exceptions import credentials_exception, auth_exp
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


ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


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


async def get_access_token(form_data: OAuth2PasswordRequestForm) -> TokenSchema | None:
    username = form_data.username
    user = await AuthService.get_user_by_username(username)
    data_dict = {"sub": username}
    access_token = create_access_token(data_dict)
    if user is None:
        raise auth_exp
    if not verify_password(form_data.password, user.hashed_password):
        raise auth_exp
    return TokenSchema(access_token=access_token)
