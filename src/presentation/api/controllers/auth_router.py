from uuid import UUID
from typing import Annotated, Tuple

from dishka import FromDishka
from dishka.integrations.fastapi import inject

from fastapi import APIRouter, Request, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import Response

from src.application.commands.auth.use_cases import (
    LoginUserUseCase,
    LogoutUserUseCase,
    RefreshAccessTokenUseCase
    )
from src.domain.auth.dtos import Token
from .aliases import security_user_annotation


auth_router = APIRouter(prefix="/auth")


@auth_router.post("/token")
@inject
async def login(
    response: Response,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    use_case: FromDishka[LoginUserUseCase],
) -> Token:
    access_token, refresh_token = await use_case.handle(form_data.username, 
                                 form_data.password)
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="strict"
    )
    return access_token # , refresh_token

@auth_router.post("/logout")
@inject
async def logout(
    request: Request,
    use_case: FromDishka[LogoutUserUseCase],
    _: security_user_annotation
) -> dict:
    refresh_token = request.cookies.get("refresh_token")
    return await use_case.handle(refresh_token)


@auth_router.post("/token/refresh")
@inject
async def refresh_access_token(
    request: Request,
    use_case: FromDishka[RefreshAccessTokenUseCase],
) -> Tuple[Token, UUID]:
    refresh_token = request.cookies.get("refresh_token")
    new_access_token, new_refresh_token = await use_case.handle(refresh_token)
    return new_access_token, new_refresh_token