from uuid import UUID
from datetime import datetime

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.common.uowed import UowedEntity


class Page(UowedEntity[UUID]):
    def __init__(
            self, 
            id: UUID,
            uow: UnitOfWork, 
            name: str,
            about: str,
            is_private: bool,
            user_id: int,   
            unblock_date: datetime | None = None,
            ) -> None:
        super().__init__(uow, id)
        self.name=name
        self.about=about
        self.is_private=is_private
        self.user_id=user_id
        self.unblock_date=unblock_date
        
    @classmethod
    def create_new(
        cls,
        id: UUID,
        uow: UnitOfWork, 
        name: str,
        about: str,
        is_private: bool,
        user_id: int,   
        unblock_date: datetime | None = None,
    ) -> "Page":
        instance = cls(id, uow, name, about, is_private, user_id, unblock_date)
        instance.mark_new()
        return instance