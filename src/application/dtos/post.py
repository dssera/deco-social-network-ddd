from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PageInPostDTO(BaseModel):
    model_config = ConfigDict(frozen=True, 
                              from_attributes=True)
    
    id: UUID
    name: str


class PostDTO(BaseModel):
    model_config = ConfigDict(frozen=True, 
                              from_attributes=True)

    id: UUID
    title: str
    body: str
    created_at: datetime
    page: PageInPostDTO | None = None


class PostPlainDTO(BaseModel):
    model_config = ConfigDict(frozen=True, 
                              from_attributes=True)

    id: UUID
    title: str
    body: str
    created_at: datetime


class PostInDTO(BaseModel):
    model_config = ConfigDict(frozen=True, 
                            from_attributes=True)

    title: str
    body: str
