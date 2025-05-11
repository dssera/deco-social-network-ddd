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
from src.infrastructure.postgres.gateways.mappers.post_data_mapper import PostDataMapper
from src.infrastructure.postgres.gateways.mappers.user_data_mapper import UserDataMapper
from src.domain.pages.entities.page import Page
from src.infrastructure.postgres.unit_of_work import UnitOfWorkImpl
from src.domain.auth.entities.user import User
from src.domain.posts.entities.post import Post


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
        page_data_mapper: DataMapper[Page],
        post_data_mapper: DataMapper[Post],
        user_data_mapper: DataMapper[User],
    ) -> Registry:
        registry = RegistryImpl() 
        registry.register_mapper(Page, page_data_mapper)
        registry.register_mapper(Post, post_data_mapper)
        registry.register_mapper(User, user_data_mapper)

        return registry

    @provide(scope=Scope.REQUEST)
    def provide_requisite_data_mapper(
        self, 
        session: AsyncSession,
    ) -> DataMapper[Page]:
        return PageDataMapper(session)
    
    @provide(scope=Scope.REQUEST)
    def provide_post_data_mapper(
        self, 
        session: AsyncSession,
    ) -> DataMapper[Post]:
        return PostDataMapper(session)
    
    @provide(scope=Scope.REQUEST)
    def provide_user_data_mapper(
        self, 
        session: AsyncSession,
    ) -> DataMapper[User]:
        return UserDataMapper(session)