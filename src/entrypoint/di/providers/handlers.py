from dishka import Provider, Scope, provide

from src.application.queries.pages import GetPagesUseCase
from src.application.commands.auth.use_cases import (
    LoginUserUseCase, 
    LogoutUserUseCase, 
    GetCurrentUserUseCase, 
    RefreshAccessTokenUseCase
    )


class HandlersProvider(Provider):
    scope = Scope.REQUEST

    get_pages_use_case = provide(GetPagesUseCase)
    login_user_use_case = provide(LoginUserUseCase)
    logout_user_use_case = provide(LogoutUserUseCase)
    get_current_user_use_case = provide(GetCurrentUserUseCase)
    refresg_access_token_use_case = provide(RefreshAccessTokenUseCase)
