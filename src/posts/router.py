from fastapi import APIRouter

from src.database import SessionDep
from src.posts.schemas import PostSchema
from src.posts.service import PostService

router = APIRouter()

@router.get("")
async def get_all_posts(session: SessionDep):
    return await PostService.get_all(session)



@router.get("/{id}")
async def get_post(session: SessionDep, id: int):
    return await PostService.get_one_by_id(session, id)


@router.post("")
async def create_post(session: SessionDep, post_data: PostSchema):
    return await PostService.create(session, post_data)

