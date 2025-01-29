from fastapi import APIRouter

from src.users.service import UserService
from src.database import SessionDep


user_router = APIRouter()

@user_router.get("")
async def get_all_users(session: SessionDep):
    return await UserService.get_all(session)
