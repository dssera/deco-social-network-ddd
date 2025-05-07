from uuid import UUID
from typing import List

from src.domain.pages.repositories.page_repository import PageRepository
from src.domain.pages.entities.page import Page
from ..dtos.page import PageDTO

class LoadPagesUseCase:
    def __init__(
            self,
            page_repository: PageRepository,
            ):
        self.page_repository = page_repository

    async def handle(
        self,
        user_id: UUID,
        **filters,
    ):
        pages: List[Page] = await self.page_repository.load_all_by_user_id(
            user_id, 
            **filters
            )
        return [PageDTO.model_validate(p) for p in pages]
        