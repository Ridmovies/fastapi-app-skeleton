from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.utils import get_hashed_password
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

