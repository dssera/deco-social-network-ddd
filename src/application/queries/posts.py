from uuid import UUID
from typing import List

from ..dtos.post import PostDTO
from src.domain.posts.entities.post import Post
from src.domain.posts.repositories.post_repository import PostRepository
from src.domain.common.unit_of_work import UnitOfWork

class GetPostsUseCase:
    def __init__(
            self,
            post_repository: PostRepository,
            ):
        self.post_repository = post_repository

    async def handle(
            self,
            limit: int = 10,
            skip: int = 0
            ) -> List[PostDTO]:
        entities: List[Post] = await self.post_repository.get_all(
            limit, skip)
        print(entities)
        print(entities[0])
        return [PostDTO.model_validate(e) for e in entities]
    
