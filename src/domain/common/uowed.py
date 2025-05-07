from src.domain.common.unit_of_work import UnitOfWork


class UowedEntity[EntityId]:
    """Класс для создания сущностей привязанных к Unit of Work"""

    def __init__(self, uow: UnitOfWork, id: EntityId) -> None:
        self.id: EntityId = id
        self.uow = uow

    def mark_new(self) -> None:
        """Пометить сущность как новая"""
        self.uow.register_new(self)

    def mark_dirty(self) -> None:
        """Пометить сущность как измененную"""
        self.uow.register_dirty(self)

    def mark_deleted(self) -> None:
        """Пометить сущщность как удаленную"""
        self.uow.register_deleted(self)
