from uuid import UUID
from datetime import datetime

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.common.uowed import UowedEntity
from ..value_objects import RoleEnum


class User(UowedEntity[UUID]):
    def __init__(
            self, 
            id: UUID,
            uow: UnitOfWork, 
            username: str,
            password: str,
            unblock_date: datetime,
            role: RoleEnum,
            email: str | None,
            tg_nickname: str | None,
            ) -> None:
        super().__init__(uow, id)
        self.username=username
        self.password=password
        self.unblock_date=unblock_date
        self.role=role
        self.email = email
        self.tg_nickname = tg_nickname
        # self.mark_new()

    @classmethod
    def create_new(
        cls,
        id: UUID,
        uow: UnitOfWork, 
        username: str,
        password: str,
        unblock_date: datetime,
        role: RoleEnum,
        email: str | None,
        tg_nickname: str | None,
    ) -> "User":
        instance = cls(id, uow, username, password, unblock_date, role, email, tg_nickname)
        instance.mark_new()
        return instance
    