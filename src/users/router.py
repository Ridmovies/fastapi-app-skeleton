from fastapi import APIRouter

from src.auth.service import UserService
from src.database import SessionDep
from src.users.schemas import UserCreate

user_router = APIRouter()


@user_router.get("")
async def get_all_users(session: SessionDep):
    return await UserService.get_all(session=session)

# @user_router.post("/register")
# async def register(user: UserCreate):
#     return ...


