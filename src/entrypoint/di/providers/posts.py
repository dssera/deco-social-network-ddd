from sqlalchemy.ext.asyncio import AsyncSession

from dishka import Provider, provide, Scope

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.posts.repositories.post_repository import PostRepository
from src.infrastructure.postgres.gateways.repositories.post_repository import PostRepositoryImpl


class PostsDomainProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_post_repository(
            self, session: AsyncSession, unit_of_work: UnitOfWork
    ) -> PostRepository:
        return PostRepositoryImpl(session, unit_of_work)
    
    
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