from uuid import UUID
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncConnection

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.pages.repositories.page_repository import (
    PageRepository
    )
from src.domain.pages.entities.page import Page
from ...tables import PageModel, UserModel
from ...converters.model_to_entity import model_to_page_entity

class PageRepositoryImpl(PageRepository):
    def __init__(
            self, 
            connection: AsyncConnection, 
            uow: UnitOfWork
            ) -> None:
        self.connection = connection
        self.uow = uow

    # async def upload_page():
    #     ...

    async def load_all_by_user_id(
        self, 
        user_id: UUID,
        tag: str | None = None,
        # need to split into few more methods
        # because these filters can be applied only separetly
        # followed_pages: bool | None = None,
        # followers_pages: bool | None = None,
        # requested_from: bool | None = None,
        # requested_in: bool | None = None,
        created_at_asc: bool = False,
        ) -> List[Page] | None:
        stmt = (
            select(PageModel)
            .where(PageModel.user_id == user_id)
            # .options(
            #     joinedload(PageModel.owner)
            #     )
        )
        result = await self.connection.execute(stmt)
        page_models: List[PageModel] = result.all()
        print("from repo: ", page_models)
        return model_to_page_entity(page_models, self.uow)

        
