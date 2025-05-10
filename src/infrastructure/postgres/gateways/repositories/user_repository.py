from uuid import UUID
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.auth.repositories.user_repository import (
    UserRepository
    )
from src.domain.auth.entities.user import User
from ...tables import UserModel, UserDataModel
from ...converters.model_to_entity import model_to_user_entity

class UserRepositoryImpl(UserRepository):
    def __init__(
            self, 
            session: AsyncSession, 
            uow: UnitOfWork
            ) -> None:
        self.session = session
        self.uow = uow

    # async def upload_page():
    #     ...

    async def get_one_or_none(
        self, 
        username: str
        ) -> User | None:
        stmt = select(UserModel).where(UserModel.username == username)
        result = await self.session.execute(stmt)
        user_model = result.scalar_one_or_none()
        if not user_model:
            return None
        
        stmt = select(UserDataModel).where(UserDataModel.user_id == user_model.id)
        result = await self.session.execute(stmt)
        user_data_model = result.scalar_one_or_none()

        return model_to_user_entity(
            user_model, 
            user_data_model, 
            self.uow
            )
        


        
