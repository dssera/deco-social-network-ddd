from typing import Protocol
from abc import abstractmethod
from datetime import timedelta
from uuid import UUID

from ..dtos import Token, TokenData


class JwtService(Protocol):
    @abstractmethod
    def create_access_token(
        self,
        username: str,
        permission: str,
        expires_delta: timedelta | None = None
        ) -> Token:
        ...

    @abstractmethod
    def create_refresh_token(
        self,
        username: str,
        expired: timedelta | None = None
        ) -> UUID:
        ...

    @abstractmethod
    def parse_token(self, 
                    token: str) -> TokenData:
        ...

    @abstractmethod
    def verify_refresh_token(self, 
                             token: UUID) -> str:
        ...

    @abstractmethod
    def delete_refresh_token(self, 
                             token: UUID):
        ...