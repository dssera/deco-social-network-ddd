from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from .value_objects import RoleEnum  


class UserDTO(BaseModel):
    username: str
    password: str
    unblock_data: datetime
    roll: RoleEnum
    user_data: "UserDataDTO"


class UserDataDTO(BaseModel):
    email: str | None = None
    tg_nickname: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
    roll: str


class TokenPairDTO(BaseModel):
    access_token: Token
    refresh_token: UUID

