from typing import List, Annotated, Dict
from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject

from fastapi import APIRouter

from src.application.queries.posts import GetPostsUseCase
from src.application.dtos.post import PostDTO, PostInDTO, PostPlainDTO
from src.application.commands.posts.use_cases import AddPostUseCase, DeletePostUseCase
from .aliases import security_user_annotation



posts_router = APIRouter(prefix="/posts")

    

@posts_router.get("")
@inject
async def get_posts(
    use_case: FromDishka[GetPostsUseCase],
    _: security_user_annotation,
    limit: int = 10,
    skip: int = 0,
) -> List[PostDTO]:
    # Здесь token — это access_token, полученный из заголовка Authorization
    return await use_case.handle(limit, skip)


@posts_router.post("")
@inject
async def add_post(
    post: PostInDTO,    
    page_id: UUID,
    use_case: FromDishka[AddPostUseCase],
    _: security_user_annotation,
) -> PostPlainDTO:
    post = await use_case.handle(post, page_id)
    return post

@posts_router.delete("")
@inject
async def delete_post(
    post_id: UUID,
    use_case: FromDishka[DeletePostUseCase],
    _: security_user_annotation,
) -> Dict[str, PostPlainDTO]:
    deleted_post = await use_case.handle(post_id)
    return {"deleted_post": deleted_post}