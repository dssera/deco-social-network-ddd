from uuid import UUID
from uuid import uuid4

from ...dtos.page import PageInDTO, PageDTO
from src.infrastructure.postgres.protocols.data_mapper import DataMapper
from src.domain.pages.entities.page import Page 

from src.domain.common.unit_of_work import UnitOfWork

class AddPageUseCase:
    def __init__(
            self,
            page_data_mapper: DataMapper[Page],
            uow: UnitOfWork,
            ):
        self.page_data_mapper = page_data_mapper
        self.uow = uow

    async def handle(
            self,
            user_id: UUID,
            page: PageInDTO
            ) -> PageDTO:
        new_page = Page(
            id=uuid4(),
            uow=self.uow,
            name=page.name,
            about=page.about,
            is_private=page.is_private,
            user_id=user_id,
            unblock_date=page.unblock_date,
            )
        print("new page: id", new_page.id)
        # added_page_model = await self.page_data_mapper.add(page)
        await self.uow.commit()
        return PageDTO.model_validate(new_page)