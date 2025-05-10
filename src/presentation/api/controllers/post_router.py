from typing import List, Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject

from fastapi import APIRouter

from src.application.queries.posts import GetPostsUseCase
from src.application.dtos.post import PostDTO
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