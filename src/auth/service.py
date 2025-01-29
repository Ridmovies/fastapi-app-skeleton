from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.jwt_utils import create_access_token, get_current_token_payload, oauth2_scheme
from src.auth.utils import get_hashed_password, verify_password
from src.database import async_session
from src.services import BaseService
from src.users.models import User
from src.users.schemas import UserCreate


class AuthService(BaseService):
    model = User

    @classmethod
    async def create_user(cls, session: AsyncSession, user: UserCreate) -> User:
        hashed_password = get_hashed_password(user.password)
        user_instance = cls.model(email=user.email, hashed_password=hashed_password)
        session.add(user_instance)
        await session.commit()
        return user_instance


    @classmethod
    async def login(cls, session: AsyncSession, user_data: UserCreate):
        email = user_data.email
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()
        data_dict = {"sub": email}
        access_token = create_access_token(data_dict)
        if user is None:
            return None
        if not verify_password(user_data.password, user.hashed_password):
            return None
        return access_token


    @classmethod
    async def get_user_by_email(cls, email: str) -> User | None:
        async with async_session() as session:
            stmt = select(User).where(User.email == email)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()


    @classmethod
    async def get_user_by_token(
            cls,
            session: AsyncSession,
            token: Annotated[str, Depends(oauth2_scheme)]
    ) -> User | None:
        payload: dict = get_current_token_payload(token)
        email: str | None = payload.get("sub")
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()




