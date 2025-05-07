from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from src.infrastructure.postgres.config import PostgresSettings


def postgres_engine(settings: PostgresSettings) -> AsyncEngine:
    engine: AsyncEngine = create_async_engine(
        url=settings.DATABASE_URL_asyncpg,
        echo=settings.PG_ECHO,
        pool_size=50,  # Размер пула (по умолчанию 5)
        max_overflow=20,  # Доп. соединения при перегрузке
        pool_timeout=30,  # Ждать до 30 сек, если пул перегружен
        pool_recycle=3600,  # Пересоздавать соединения каждый час
        pool_pre_ping=True,  # Проверять соединения перед использованием
    )
    return engine
