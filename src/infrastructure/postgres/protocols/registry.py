from abc import abstractmethod
from typing import Protocol

from src.domain.common.uowed import UowedEntity
from src.infrastructure.postgres.protocols.data_mapper import DataMapper


class Registry(Protocol):
    @abstractmethod
    def register_mapper(self, entity: type[UowedEntity], mapper: DataMapper) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def get_mapper(self, entity: type[UowedEntity]) -> DataMapper:
        raise NotImplementedError("Method must be implemented by subclasses")
