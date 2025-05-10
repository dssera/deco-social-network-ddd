from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine, 
    AsyncSession,
    async_sessionmaker
    )

from dishka import Provider, provide, Scope

from redis import Redis

from src.config.db_settings import engine
from src.domain.common.unit_of_work import UnitOfWork
from src.infrastructure.postgres.protocols.registry import Registry
from src.infrastructure.postgres.registry import RegistryImpl
from src.infrastructure.postgres.protocols.data_mapper import DataMapper
from src.infrastructure.postgres.gateways.mappers.page_data_mapper import PageDataMapper
from src.domain.pages.entities.page import Page
from src.infrastructure.postgres.unit_of_work import UnitOfWorkImpl
from src.domain.pages.repositories.page_repository import PageRepository
from src.infrastructure.postgres.gateways.repositories.page_repository import PageRepositoryImpl
from src.domain.auth.repositories.user_repository import UserRepository
from src.infrastructure.postgres.gateways.repositories.user_repository import UserRepositoryImpl
from src.domain.auth.services.hasher_service import HasherService
from src.infrastructure.services.auth.hasher_service import HasherServiceImpl
from src.domain.auth.services.jwt_service import JwtService
from src.infrastructure.services.auth.jwt_service import JwtServiceImpl


class PostgresDatabaseProvider(Provider):

    # @provide(scope=Scope.APP)
    # def provide_postgres_config(self) -> PostgresConfig:
    #     return PostgresConfig()

    @provide(scope=Scope.APP)
    def provide_postgres_engine(
        self,
    ) -> AsyncEngine:
        return engine

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_postgres_connection(
        self,
        engine: AsyncEngine,
    ) -> AsyncGenerator[AsyncSession, None]:
        async_session_factory = async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
        )
        async with async_session_factory() as session:
            yield session


    @provide(scope=Scope.REQUEST)
    def provide_unit_of_work(
        self, session: AsyncSession, registry: Registry
    ) -> UnitOfWork:
        return UnitOfWorkImpl(
            registry=registry, 
            session=session
            )
    
    # @provide(scope=Scope.REQUEST)
    # def provide_unit_of_work(
    #     self, connection: AsyncSession, registry: Registry
    # ) -> UnitOfWork:
    #     return UnitOfWorkImpl(
    #         registry=registry, 
    #         session=connection
    #         )
    
    @provide(scope=Scope.REQUEST)
    def provide_registry(
        self, 
        page_data_mapper: DataMapper[Page]
    ) -> Registry:
        registry = RegistryImpl() 
        registry.register_mapper(Page, page_data_mapper)

    @provide(scope=Scope.REQUEST)
    def provide_requisite_data_mapper(
        self, 
        session: AsyncSession
    ) -> DataMapper[Page]:
        return PageDataMapper(session)