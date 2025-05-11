from src.domain.common.uowed import UowedEntity
from src.infrastructure.postgres.protocols.data_mapper import DataMapper
from src.infrastructure.postgres.protocols.registry import Registry


class RegistryImpl(Registry):
    def __init__(self):
        # one data type : one mapper
        self.data_mappers: dict[type[UowedEntity], DataMapper] = {}

    def register_mapper(self, entity: type[UowedEntity], mapper: DataMapper) -> None:
        self.data_mappers[entity] = mapper # ЧЕКНИ РЕПУ ДИМЫ И СКАЖИ ЕМУ
        print(f"i have registered mapper for entity: {entity}")
        print(self.data_mappers)

    def get_mapper(self, entity: type[UowedEntity]) -> DataMapper:
        mapper = self.data_mappers[entity]
        if not mapper:
            raise ValueError(f"Mapper for {entity} not registered")
        return mapper
