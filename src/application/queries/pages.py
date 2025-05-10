from uuid import UUID
from typing import List

from ..dtos.page import PageDTO
from src.domain.pages.entities.page import Page
from src.domain.pages.repositories.page_repository import PageRepository
from src.domain.common.unit_of_work import UnitOfWork

class GetPagesUseCase:
    def __init__(
            self,
            page_repository: PageRepository,
            ):
        self.page_repository = page_repository

    async def handle(
            self,
            user_id: UUID,
            **filters,
            ) -> List[PageDTO]:
        entities: List[Page] = await self.page_repository.get_all_by_user_id(
            user_id, **filters)
        return [PageDTO.model_validate(e) for e in entities]
    
