from sqlalchemy.ext.asyncio import AsyncConnection

from ...protocols.data_mapper import DataMapper
from src.domain.pages.entities.page import Page

class PageDataMapper(DataMapper[Page]):
    def __init__(
            self,
            connection: AsyncConnection
            ):
        self.connection = connection
        
    async def add(self, entity: Page) -> None:
        raise NotImplementedError("Not impl yet.")

    async def delete(self, entity: Page) -> None:
        raise NotImplementedError("Not impl yet.")

    async def update(self, entity: Page) -> None:
        raise NotImplementedError("Not impl yet.")
