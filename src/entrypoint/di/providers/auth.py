from sqlalchemy.ext.asyncio import AsyncSession

from dishka import Provider, provide, Scope

from redis import Redis

from fastapi.security import OAuth2PasswordBearer

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.auth.repositories.user_repository import UserRepository
from src.infrastructure.postgres.gateways.repositories.user_repository import UserRepositoryImpl
from src.domain.auth.services.hasher_service import HasherService
from src.infrastructure.services.auth.hasher_service import HasherServiceImpl
from src.domain.auth.services.jwt_service import JwtService
from src.infrastructure.services.auth.jwt_service import JwtServiceImpl


class AuthDomainProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_user_repository(
            self, session: AsyncSession, unit_of_work: UnitOfWork
    ) -> UserRepository:
        return UserRepositoryImpl(session, unit_of_work)
    
    @provide(scope=Scope.REQUEST)
    def provide_jwt_service(
            self,
            redis: Redis,
    ) -> JwtService:
        return JwtServiceImpl(redis)
    
    @provide(scope=Scope.REQUEST)
    def provide_hasher_service(
            self,
    ) -> HasherService:
        return HasherServiceImpl()
    
    @provide(scope=Scope.APP)
    def provide_redis(
            self,
    ) -> Redis:
        return Redis()
    
    @provide(scope=Scope.APP)
    def provide_oauth2_schema(
            self,
    ) -> OAuth2PasswordBearer:
        return OAuth2PasswordBearer(
            tokenUrl="/auth/token",
            )
    
    # @provide(scope=Scope.REQUEST)
    # def provide_merchant_repository(
    #     self, connection: AsyncConnection
    # ) -> MerchantRepository:
    #     return MerchantRepositoryImpl(connection)
    
    
    # @provide(scope=Scope.REQUEST)
    # def provide_merchant_repository(
    #     self, connection: AsyncConnection, unit_of_work: UnitOfWork
    # ) -> MerchantRepository:
    #     return MerchantRepositoryImpl(unit_of_work, connection)