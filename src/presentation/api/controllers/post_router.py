from uuid import UUID
from typing import List

from dishka import FromDishka
from dishka.integrations.fastapi import inject

from fastapi import APIRouter, Security

from src.application.queries.posts import GetPostsUseCase
from src.application.dtos.post import PostDTO
from src.presentation.common.fastapi_dependencies import oauth2_schema



posts_router = APIRouter(prefix="/posts")

    
@posts_router.get("",
                  dependencies=[Security(oauth2_schema)])
@inject
async def get_posts(
    use_case: FromDishka[GetPostsUseCase],
    limit: int = 10,
    skip: int = 0,
) -> List[PostDTO]:
    return await use_case.handle(limit, skip)
