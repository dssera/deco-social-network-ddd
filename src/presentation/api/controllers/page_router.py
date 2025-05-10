from uuid import UUID
from typing import Annotated, List

from dishka import FromDishka
from dishka.integrations.fastapi import inject

from fastapi import APIRouter, Security

from src.application.queries.pages import GetPagesUseCase
from src.presentation.common.fastapi_dependencies import oauth2_schema
from src.application.dtos.auth import UserDTO
from src.domain.auth.value_objects import RoleEnum
from src.application.dtos.page import PageDTO
from ...common.fastapi_dependencies import get_current_user
from .aliases import security_user_annotation


pages_router = APIRouter(prefix="/pages")

    
@pages_router.get("",
                  # dependencies=[Security(oauth2_schema)],
                  )
@inject
async def get_pages_filtered(
    user: security_user_annotation,
    use_case: FromDishka[GetPagesUseCase],
) -> List[PageDTO]:
    return await use_case.handle(user.id)


# @pages_router.post("",
#                   dependencies=[Security(oauth2_schema)])
# @inject
# async def add_page(
#     user_id: UUID,
#     # use_case: FromDishka[GetPagesUseCase],
# ) -> None:
#     return await use_case.handle(user_id)