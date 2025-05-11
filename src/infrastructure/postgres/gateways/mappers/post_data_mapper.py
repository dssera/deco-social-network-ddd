from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, delete, update

from src.domain.posts.entities.post import Post
from src.domain.common.unit_of_work import UnitOfWork
from ...protocols.data_mapper import DataMapper
from ...converters.entity_to_dict import post_entity_to_dict
from ...tables import PostModel

class PostDataMapper(DataMapper[Post]):
    def __init__(
            self,
            session: AsyncSession,
            ):
        self.session = session
        
    async def add(self, entity: Post) -> None:
        data_dict = post_entity_to_dict(entity)
        query = insert(PostModel).values(data_dict)
        await self.session.execute(query)

    async def delete(self, entity: Post) -> None:
        query = delete(PostModel).where(PostModel.id == entity.id)
        await self.session.execute(query)

    async def update(self, entity: Post) -> None:
        data_dict = post_entity_to_dict(entity)
        query = update(PostModel).where(PostModel.id == entity.id).values(data_dict)
        await self.session.execute(query)