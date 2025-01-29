# to get a string like this run:
# openssl rand -hex 32
from datetime import timedelta, timezone, datetime
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy import select
from starlette import status

from src.database import async_session
from src.users.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_token_payload(
    token: str,
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token error: {e}",
        )
    return payload


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        # token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    async with async_session() as session:
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()
    if user is None:
        raise credentials_exception
    return user