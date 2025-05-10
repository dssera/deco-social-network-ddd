from uuid import UUID
from typing import Tuple

from src.domain.auth.services.jwt_service import JwtService
from src.domain.auth.services.hasher_service import HasherService
from src.domain.auth.repositories.user_repository import UserRepository
from src.domain.auth.dtos import TokenPairDTO, Token, TokenData
from src.domain.auth.entities.user import User
from .exceptions import UserDoesntExist, InvalidPassword
from ...dtos.auth import UserDTO


class LoginUserUseCase:
    def __init__(
            self,
            user_repo: UserRepository,
            jwt_service: JwtService,
            hasher_service: HasherService,
            ):
        self.user_repo = user_repo
        self.jwt_service = jwt_service
        self.hasher_service = hasher_service

    async def handle(
            self,
            username: str,
            password: str,
            ) -> Tuple[Token, UUID]:
        user: User = await self.user_repo.get_one_or_none(
            username)
        if not user:
            raise UserDoesntExist()
        if not self.hasher_service.verify_password(password, user.password):
            raise InvalidPassword()
        
        access_token = self.jwt_service.create_access_token(
            user.username, user.role
        )
        refresh_token = self.jwt_service.create_refresh_token(username)
        return access_token, refresh_token
        

class LogoutUserUseCase:
    def __init__(
            self,
            jwt_service: JwtService,
            ):
        self.jwt_service = jwt_service

    async def handle(
            self,
            refresh_token: UUID):
        self.jwt_service.delete_refresh_token(refresh_token)
        return {"message": "Logged out successfully"}


class RefreshAccessTokenUseCase:
    def __init__(
            self,
            jwt_service: JwtService,
            user_repo: UserRepository,
            ):
        self.jwt_service = jwt_service
        self.user_repo = user_repo


    async def handle(
            self,
            refresh_token: UUID,
            ) -> Tuple[Token, UUID]:
        username = self.jwt_service.verify_refresh_token(refresh_token)
        user: User = await self.user_repo.get_one_or_none(username)
        new_access_token = self.jwt_service.create_access_token(
            user.username, user.role)
        new_refresh_token = self.jwt_service.create_refresh_token(
            user.username)
        return new_access_token, new_refresh_token


class GetCurrentUserUseCase:
    def __init__(
            self,
            user_repo: UserRepository,
            jwt_service: JwtService,
            hasher_service: HasherService,
            ):
        self.user_repo = user_repo
        self.jwt_service = jwt_service
        self.hasher_service = hasher_service

    async def handle(
            self, 
            access_token: Token
            ) -> UserDTO:
        data: TokenData = self.jwt_service.parse_token(access_token)
        user: User = await self.user_repo.get_one_or_none(data.username)
        return UserDTO.model_validate(user)