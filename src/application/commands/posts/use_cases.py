from uuid import UUID, uuid4
from datetime import datetime

from src.infrastructure.postgres.protocols.data_mapper import DataMapper
from src.domain.posts.entities.post import Post
from src.domain.common.unit_of_work import UnitOfWork
from ...dtos.post import PostDTO, PostInDTO, PostPlainDTO
from src.domain.posts.repositories.post_repository import PostRepository

class AddPostUseCase:
    def __init__(
            self,
            uow: UnitOfWork,
            ):
        self.uow = uow

    async def handle(
            self,
            post: PostInDTO,
            page_id: UUID,
            ) -> PostPlainDTO:
        print(page_id)
        new_post = Post.create_new(
            id=uuid4(),
            uow=self.uow,
            title=post.title,
            body=post.body,
            created_at=datetime.now(),
            page_id=page_id,
            )
        print(page_id)
        await self.uow.commit()
        return PostPlainDTO.model_validate(new_post)
    

class DeletePostUseCase:
    def __init__(
            self,
            post_repo: PostRepository,
            uow: UnitOfWork,
            ):
        self.post_repo = post_repo
        self.uow = uow

    async def handle(
            self,
            post_id: UUID,
            ) -> PostPlainDTO:
        post_to_delete = await self.post_repo.get_one_or_none(post_id)
        post_to_delete.mark_deleted()
        await self.uow.commit()
        return PostPlainDTO.model_validate(post_to_delete)


    

