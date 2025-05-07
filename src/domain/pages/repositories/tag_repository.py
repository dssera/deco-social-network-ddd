from typing import Protocol
from abc import abstractmethod

from ..entities.tag import Tag

class TagRepository(Protocol):

    @abstractmethod
    async def load_by_name(self, name: str) -> Tag | None:
        raise NotImplementedError("Method must be implemented by subclasses")