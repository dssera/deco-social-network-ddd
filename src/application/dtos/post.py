from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict

class PostDTO(BaseModel):
    model_config = ConfigDict(frozen=True, 
                              from_attributes=True)

    id: UUID
    title: str
    body: str
    created_at: datetime
    page: "PageDTO"

class PageDTO(BaseModel):
    model_config = ConfigDict(frozen=True, 
                              from_attributes=True)
    
    id: UUID
    name: str
    # about: str
    # is_private: bool
    # unblock_date: datetime | None = None
    # user_id: UUID
