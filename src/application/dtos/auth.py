from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

from src.domain.auth.value_objects import RoleEnum  


class UserDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str
    password: str
    unblock_data: datetime | None = None
    role: RoleEnum
    email: str | None = None
    tg_nickname: str | None = None


# class UserDataDTO(BaseModel):
#     model_config = ConfigDict(from_attributes=True)

#     email: str | None = None
#     tg_nickname: str | None = None