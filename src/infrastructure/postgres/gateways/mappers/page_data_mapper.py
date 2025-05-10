from sqlalchemy.ext.asyncio import AsyncSession

from ...protocols.data_mapper import DataMapper
from src.domain.pages.entities.page import Page

class PageDataMapper(DataMapper[Page]):
    def __init__(
            self,
            session: AsyncSession
            ):
        self.connection = session
        
    async def add(self, entity: Page) -> None:
        raise NotImplementedError("Not impl yet.")

    async def delete(self, entity: Page) -> None:
        raise NotImplementedError("Not impl yet.")

    async def update(self, entity: Page) -> None:
        raise NotImplementedError("Not impl yet.")
