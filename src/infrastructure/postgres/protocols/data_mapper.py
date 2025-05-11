from abc import abstractmethod
from typing import Protocol
from src.domain.common.unit_of_work import UnitOfWork



class DataMapper[Entity](Protocol):
    @abstractmethod
    async def add(self, entity: Entity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def delete(self, entity: Entity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def update(self, entity: Entity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
