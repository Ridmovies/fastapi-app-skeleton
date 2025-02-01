from fastapi import APIRouter, Depends
from starlette import status

from src.auth.jwt_utils import get_current_user
from src.database import SessionDep
from src.posts.schemas import PostSchema, PostOutSchema
from src.posts.service import PostService
from src.users.models import User

router = APIRouter()


@router.get("")
async def get_all_posts(session: SessionDep):
    return await PostService.get_all(session)


@router.get("/{id}")
async def get_post(session: SessionDep, id: int):
    return await PostService.get_one_by_id(session, id)


@router.post("")
async def create_post(
        session: SessionDep,
        post_data: PostSchema,
        current_user: User = Depends(get_current_user)
):
    return await PostService.create(session, post_data, current_user.id)


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
        session: SessionDep,
        post_id: int,
        current_user: User = Depends(get_current_user)
):
    return await PostService.delete(session, post_id, current_user.id)


@router.put("", response_model=PostOutSchema, status_code=status.HTTP_200_OK)
async def update_post(
        session: SessionDep,
        post_id: int,
        post_data: PostSchema,
        current_user: User = Depends(get_current_user),
):
    return await PostService.update(session, post_id, post_data, current_user.id)


