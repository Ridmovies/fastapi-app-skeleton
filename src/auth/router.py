from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.jwt_utils import get_current_user, get_access_token
from src.auth.service import AuthService
from src.database import SessionDep
from src.users.models import User
from src.users.schemas import UserCreate, UserSchema

auth_router = APIRouter()


@auth_router.post("/register", response_model=UserSchema)
async def register(session: SessionDep, user: UserCreate):
    return await AuthService.create_user(session, user)


@auth_router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return await get_access_token(form_data)

# @auth_router.post("/api/logout")
# async def logout(token: str = Depends(settings.TOKEN_MANAGER)):
#     views.set_expiry(0, token)
#     return {"response": "Logged out"}


@auth_router.get("/me", response_model=UserSchema)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
