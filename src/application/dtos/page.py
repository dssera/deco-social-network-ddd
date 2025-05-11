from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict

class PageDTO(BaseModel):
    model_config = ConfigDict(frozen=True, 
                              from_attributes=True)

    id: UUID
    name: str
    about: str
    is_private: bool
    user_id: UUID
    unblock_date: datetime | None = None

class PageInDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    about: str
    is_private: bool = False
    unblock_date: datetime | None = None
    