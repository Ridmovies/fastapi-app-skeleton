from fastapi import APIRouter

from src.auth.service import AuthService
from src.database import SessionDep
from src.users.schemas import UserCreate

auth_router = APIRouter()

@auth_router.post("/register")
async def register(session: SessionDep, user: UserCreate):
    return await AuthService.create_user(session, user)


@auth_router.post("/login")
async def login(session: SessionDep, user: UserCreate):
    return await AuthService.login(session, user)