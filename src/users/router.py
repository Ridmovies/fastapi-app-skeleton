from fastapi import APIRouter

from src.users.schemas import UserSchema
from src.users.service import UserService
from src.database import SessionDep


user_router = APIRouter()

@user_router.get("", response_model=list[UserSchema])
async def get_all_users(session: SessionDep):
    return await UserService.get_all(session)
