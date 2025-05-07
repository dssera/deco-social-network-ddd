from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.entrypoint.di.providers.postgres import PostgresDatabaseProvider
from src.entrypoint.di.providers.auth import AuthDomainProvider
from src.entrypoint.di.providers.pages import PagesDomainProvider
from .handlers import HandlersProvider


def setup_container() -> AsyncContainer:
    return make_async_container(
        PostgresDatabaseProvider(),
        AuthDomainProvider(),
        PagesDomainProvider(),
        HandlersProvider(),
    )


def setup_di(app: FastAPI) -> None:
    setup_dishka(setup_container(), app)
