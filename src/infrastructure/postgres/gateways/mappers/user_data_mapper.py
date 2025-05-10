from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, update, delete

from src.domain.auth.entities.user import User
from ...protocols.data_mapper import DataMapper
from ...converters.entity_to_dict import user_entity_to_dict
from ...tables import UserModel

class UserDataMapper(DataMapper[User]):
    def __init__(
            self,
            session: AsyncSession
            ):
        self.connection = session
        
    async def add(self, entity: User) -> None:
        data_dict = user_entity_to_dict(entity)
        query = insert(UserModel).values(data_dict)
        self.session.execute(query)

    async def delete(self, entity: User) -> None:
        query = delete(UserModel).where(UserModel.id == entity.id)
        self.session.execute(query)

    async def update(self, entity: User) -> None:
        data_dict = user_entity_to_dict(entity)
        query = update(UserModel).where(UserModel.id == entity.id).values(data_dict)
        self.session.execute(query)
