from datetime import datetime
from uuid import UUID

from pydantic import BaseModel




class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
    roll: str


class TokenPairDTO(BaseModel):
    access_token: Token
    refresh_token: UUID

