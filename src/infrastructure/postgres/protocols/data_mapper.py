from abc import abstractmethod
from typing import Protocol


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
