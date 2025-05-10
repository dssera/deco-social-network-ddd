from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.entrypoint.di.providers.postgres import PostgresDatabaseProvider
from src.entrypoint.di.providers.auth import AuthDomainProvider
from src.entrypoint.di.providers.pages import PagesDomainProvider
from src.entrypoint.di.providers.posts import PostsDomainProvider
from src.entrypoint.di.providers.handlers import HandlersProvider



def setup_container() -> AsyncContainer:
    return make_async_container(
        PostgresDatabaseProvider(),
        AuthDomainProvider(),
        PagesDomainProvider(),
        HandlersProvider(),
        PostsDomainProvider(),
    )


def setup_di(app: FastAPI) -> None:
    setup_dishka(setup_container(), app)
