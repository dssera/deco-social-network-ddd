from uuid import UUID
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.posts.repositories.post_repository import (
    PostRepository
    )
from src.domain.posts.entities.post import Post
from ...tables import PostModel, PageModel
from ...converters.model_to_entity import model_to_post_entity


class PostRepositoryImpl(PostRepository):
    def __init__(
            self, 
            session: AsyncSession, 
            uow: UnitOfWork
            ) -> None:
        self.session = session
        self.uow = uow

    async def get_all(
        self, 
        limit: int = 10,
        offset: int = 0,
        ) -> List[Post] | None:
            stmt = (
                select(PostModel)
                .options(
                    joinedload(PostModel.page)
                    )
                .limit(limit)
                .offset(offset)
            )
            result = await self.session.execute(stmt)
            posts = list(result.scalars())
            return model_to_post_entity(posts, self.uow)
    
    async def get_one_or_none(
        self, 
        post_id: UUID
        ) -> Post | None:
        stmt = (
             select(PostModel)
             .where(PostModel.id == post_id)
        )
        result = await self.session.execute(stmt)
        post = result.scalar_one_or_none()
        return model_to_post_entity(post, self.uow)
