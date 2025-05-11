from uuid import UUID

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.common.uowed import UowedEntity


class Tag(UowedEntity[UUID]):
    def __init__(
            self, 
            id: UUID,
            uow: UnitOfWork, 
            name: str,
            ) -> None:
        super().__init__(uow, id)
        self.name=name
        self.mark_new()