from typing import Annotated

from fastapi import APIRouter, Depends

from src.auth.jwt_utils import (
    get_current_user,
    create_access_token,
    create_refresh_token,
    validate_auth_user, http_bearer, get_current_user_for_refresh,
)
from src.auth.schemas import TokenSchema
from src.auth.service import AuthService
from src.database import SessionDep
from src.users.models import User
from src.users.schemas import UserCreate, UserSchema

auth_router = APIRouter(dependencies=[Depends(http_bearer)])


@auth_router.post("/register", response_model=UserSchema)
async def register(session: SessionDep, user: UserCreate):
    return await AuthService.create_user(session, user)


@auth_router.post("/login")
async def login(user: UserSchema = Depends(validate_auth_user)):
    access_token = create_access_token(user=user)
    refresh_token = create_refresh_token(user=user)
    return TokenSchema(
        access_token=access_token,
        refresh_token=refresh_token,
    )

@auth_router.get("/me", response_model=UserSchema)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@auth_router.post(
    "/refresh",
    response_model=TokenSchema,
    response_model_exclude_none=True,
)
async def auth_refresh_jwt(
    user: UserSchema = Depends(get_current_user_for_refresh),
):
    access_token = create_access_token(user)
    return TokenSchema(
        access_token=access_token,
    )
