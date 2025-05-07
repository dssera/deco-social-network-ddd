from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject

from fastapi import APIRouter, Security

from src.application.queries.pages import GetPagesUseCase
from src.presentation.common.fastapi_dependencies import oauth2_schema


pages_router = APIRouter(prefix="/pages")

    
@pages_router.get("",
                  dependencies=[Security(oauth2_schema)])
@inject
async def get_pages_filtered(
    user_id: UUID,
    use_case: FromDishka[GetPagesUseCase],
) -> None:
    return await use_case.handle(user_id)