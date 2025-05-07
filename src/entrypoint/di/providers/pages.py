from sqlalchemy.ext.asyncio import AsyncConnection

from dishka import Provider, provide, Scope

from src.domain.common.unit_of_work import UnitOfWork
from src.domain.pages.repositories.page_repository import PageRepository
from src.infrastructure.postgres.gateways.repositories.page_repository import PageRepositoryImpl


class PagesDomainProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_page_repository(
            self, connection: AsyncConnection, unit_of_work: UnitOfWork
    ) -> PageRepository:
        return PageRepositoryImpl(connection, unit_of_work)
    
    
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