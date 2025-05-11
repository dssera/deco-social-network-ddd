from typing import Protocol, List
from abc import abstractmethod
from uuid import UUID


from ..entities.post import Post


class PostRepository(Protocol):

    @abstractmethod
    async def get_all(
        self, 
        limit: int = 10,
        skip: int = 0,
        # user_id: UUID,
        # tag: str | None = None,
        # need to split into few more methods
        # because these filters can be applied only separetly
        # followed_pages: bool | None = None,
        # followers_pages: bool | None = None,
        # requested_from: bool | None = None,
        # requested_in: bool | None = None,
        # created_at_asc: bool = False,
        ) -> List[Post] | None:
        raise NotImplementedError("Method must be implemented by subclasses")
    
    @abstractmethod
    async def get_one_or_none(
        self, 
        post_id: UUID
        ) -> Post | None:
        raise NotImplementedError("Method must be implemented by subclasses")