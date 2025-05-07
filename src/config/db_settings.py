from os import getenv as env

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


load_dotenv()


class Base(AsyncAttrs, DeclarativeBase):
    ...


DATABASE_URL = f"postgresql+asyncpg://{env('PG_USER')}:{env('PG_PASSWORD')}@{env('PG_HOST')}:{env('PG_PORT')}/{env('PG_DB')}"
SYNC_DATABASE_URL = f"postgresql+psycopg://{env('PG_USER')}:{env('PG_PASSWORD')}@{env('PG_HOST')}:{env('PG_PORT')}/{env('PG_DB')}"

engine = create_async_engine(
    url=DATABASE_URL,
    pool_size=5,
    max_overflow=5,
    pool_timeout=30,
    pool_recycle=3600,
)

async_session = async_sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)
