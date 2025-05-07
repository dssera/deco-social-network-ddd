from datetime import timedelta, timezone, datetime
from uuid import UUID, uuid4

import jwt

from redis import Redis

from src.domain.auth.services.jwt_service import JwtService
from src.domain.auth.dtos import Token, TokenData
from .exceptions import jwt_is_expired_exc

class JwtServiceImpl(JwtService):
    def __init__(
            self,
            redis: Redis
            ):
        self.redis = redis

    def create_access_token(
        self,
        username: str,
        permission: str,
        expires_delta: timedelta | None = None
        ) -> Token:
        to_encode = {"sub": username, "scopes": permission}
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(hours=2)
        # jti to make every token unique - even if paylaod is similar
        to_encode.update({"exp": expire, 
                          "jti": str(uuid4())})
        encoded_jwt = jwt.encode(
            to_encode, "SECRET_JWT_KEY", "HS256"
            )
        return Token(token_type="Bearer", access_token=encoded_jwt)

    def create_refresh_token(
        self,
        username: str,
        expired: timedelta | None = None
        ) -> UUID:
        refresh_token = uuid4()
        self.redis.setex(str(refresh_token), 36000, username)
        return refresh_token

    def parse_token(self, 
                    token: str) -> TokenData:
        payload = jwt.decode(token.encode(), "SECRET_JWT_KEY", ["HS256"])
        username: str = payload.get("sub")
        if not username:
            raise jwt_is_expired_exc
        token_scopes = payload.get("scopes", "")
        token_data = TokenData(roll=token_scopes, 
                               username=username)
        return token_data
        

    def verify_refresh_token(self, token: UUID) -> str | None:
        bytes = self.redis.get(str(token))
        string = bytes.decode()
        return string

    def delete_refresh_token(self, token: UUID):
        self.redis.delete(str(token))