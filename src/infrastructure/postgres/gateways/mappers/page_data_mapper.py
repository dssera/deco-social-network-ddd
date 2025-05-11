from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, update, delete

from src.domain.pages.entities.page import Page
from src.domain.common.unit_of_work import UnitOfWork
from ...protocols.data_mapper import DataMapper
from ...converters.entity_to_dict import page_entity_to_dict
from ...converters.model_to_entity import model_to_page_entity
from ...tables import PageModel



class PageDataMapper(DataMapper[Page]):
    def __init__(
            self,
            session: AsyncSession,
            ):
        self.session = session
        
    async def add(self, entity: Page) -> PageModel:
        data_dict = page_entity_to_dict(entity)
        query = insert(PageModel).values(data_dict).returning(PageModel)
        result = await self.session.execute(query)
        return result.scalar()

    async def delete(self, entity: Page) -> None:
        query = delete(PageModel).where(PageModel.id == entity.id)
        await self.session.execute(query)

    async def update(self, entity: Page) -> None:
        data_dict = page_entity_to_dict(entity)
        query = update(PageModel).where(PageModel.id == entity.id).values(data_dict)
        await self.session.execute(query)
