from uuid import UUID
from datetime import datetime

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.common.uowed import UowedEntity
from src.domain.pages.entities.page import Page


class Post(UowedEntity[UUID]):
    def __init__(
            self, 
            id: UUID,
            uow: UnitOfWork, 
            title: str,
            body: str,
            created_at: datetime,
            page_id: UUID,
            page: Page | None = None
            ) -> None:
        super().__init__(uow, id)
        self.title=title
        self.body=body
        self.created_at=created_at
        self.page_id = page_id
        self.page = page
        self.mark_new()
    