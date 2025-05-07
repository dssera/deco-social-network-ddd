from typing import Protocol, List
from abc import abstractmethod
from uuid import UUID


from ..entities.user import User

class UserRepository(Protocol):

    @abstractmethod
    async def get_one_or_none(
        self, 
        username: str
        ) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")