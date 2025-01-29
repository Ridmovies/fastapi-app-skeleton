from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer


from src.auth.jwt_utils import get_current_token_payload, get_current_user
from src.auth.service import AuthService
from src.database import SessionDep
from src.users.models import User
from src.users.schemas import UserCreate, UserSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")
auth_router = APIRouter()

@auth_router.post("/register")
async def register(session: SessionDep, user: UserCreate):
    return await AuthService.create_user(session, user)


@auth_router.post("/login")
async def login(session: SessionDep, user: UserCreate):
    return await AuthService.login(session, user)


@auth_router.get("/payload")
async def payload(token: str):
    return get_current_token_payload(token)



@auth_router.get("/users/me/", response_model=UserSchema)
async def read_users_me(session: SessionDep, token: str):
    return await AuthService.get_user_by_token(session, token)


