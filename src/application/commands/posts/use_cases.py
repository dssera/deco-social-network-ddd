from uuid import UUID, uuid4
from datetime import datetime

from src.infrastructure.postgres.protocols.data_mapper import DataMapper
from src.domain.posts.entities.post import Post
from src.domain.common.unit_of_work import UnitOfWork
from ...dtos.post import PostDTO, PostInDTO, PostPlainDTO

class AddPostUseCase:
    def __init__(
            self,
            post_data_mapper: DataMapper[Post],
            uow: UnitOfWork,
            ):
        self.post_data_mapper = post_data_mapper
        self.uow = uow

    async def handle(
            self,
            post: PostInDTO,
            page_id: UUID,
            ) -> PostPlainDTO:
        print(page_id)
        new_post = Post(
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