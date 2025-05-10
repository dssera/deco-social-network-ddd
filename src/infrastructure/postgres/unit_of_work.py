from typing import List, DefaultDict

from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.common.uowed import UowedEntity
from src.infrastructure.postgres.protocols.registry import Registry


class UnitOfWorkImpl(UnitOfWork):
    def __init__(
        self,
        registry: Registry,
        session: AsyncSession,
    ) -> None:
        self.new: dict[type[UowedEntity], list[UowedEntity]] = DefaultDict(list)
        self.dirty: dict[type[UowedEntity], list[UowedEntity]] = DefaultDict(list)
        self.deleted: dict[type[UowedEntity], list[UowedEntity]] = DefaultDict(list)
        self.registry = registry
        self.session = session

    def register_new(self, entity: UowedEntity) -> None:
        self.new[type(entity)].append(entity)

    def register_dirty(self, entity: UowedEntity) -> None:
        self.dirty[type(entity)].append(entity)

    def register_deleted(self, entity: UowedEntity) -> None:
        self.deleted[type(entity)].append(entity)

    async def commit(self) -> None:
        for entity_type, entities in self.new.items():
            if entities:
                mapper = self.registry.get_mapper(entity_type)
                for entity in entities:
                    await mapper.add(entity)

        for entity_type, entities in self.dirty.items():
            if entities:
                mapper = self.registry.get_mapper(entity_type)
                for entity in entities:
                    await mapper.update(entity)

        for entity_type, entities in self.deleted.items():
            if entities:
                mapper = self.registry.get_mapper(entity_type)
                for entity in entities:
                    await mapper.delete(entity)

        await self.session.commit()
