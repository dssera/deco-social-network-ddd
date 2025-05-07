from typing import Protocol, List
from abc import abstractmethod
from uuid import UUID


from ..entities.page import Page

class PageRepository(Protocol):

    @abstractmethod
    async def load_all_by_user_id(
        self, 
        user_id: UUID,
        tag: str | None = None,
        # need to split into few more methods
        # because these filters can be applied only separetly
        # followed_pages: bool | None = None,
        # followers_pages: bool | None = None,
        # requested_from: bool | None = None,
        # requested_in: bool | None = None,
        created_at_asc: bool = False,
        ) -> List[Page] | None:
        raise NotImplementedError("Method must be implemented by subclasses")