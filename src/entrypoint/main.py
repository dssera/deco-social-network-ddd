from fastapi import FastAPI

from src.entrypoint.di.providers.main import setup_di
# from src.presentation.api.controllers.exceptions import setup_exception_handlers


def app_factory() -> FastAPI:
    app = FastAPI()
    # setup_controllers(app) #noqa: E800
    setup_di(app)
    # setup_exception_handlers(app)
    return app
