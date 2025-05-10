from pydantic import BaseModel
from datetime import datetime

from src.domain.auth.value_objects import RoleEnum  


class UserDTO(BaseModel):
    username: str
    password: str
    unblock_data: datetime
    roll: RoleEnum
    user_data: "UserDataDTO"


class UserDataDTO(BaseModel):
    email: str | None = None
    tg_nickname: str | None = None