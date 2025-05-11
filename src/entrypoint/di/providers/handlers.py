from dishka import Provider, Scope, provide

from src.application.queries.pages import GetPagesUseCase
from src.application.commands.auth.use_cases import (
    LoginUserUseCase, 
    LogoutUserUseCase, 
    GetCurrentUserUseCase, 
    RefreshAccessTokenUseCase
    )
from src.application.queries.posts import GetPostsUseCase
from src.application.commands.pages.use_cases import AddPageUseCase
from src.application.commands.posts.use_cases import AddPostUseCase



class HandlersProvider(Provider):
    scope = Scope.REQUEST

    get_pages_use_case = provide(GetPagesUseCase)
    login_user_use_case = provide(LoginUserUseCase)
    logout_user_use_case = provide(LogoutUserUseCase)
    get_current_user_use_case = provide(GetCurrentUserUseCase)
    refresh_access_token_use_case = provide(RefreshAccessTokenUseCase)
    get_posts_use_case = provide(GetPostsUseCase)
    add_page_use_case = provide(AddPageUseCase)
    add_post_use_case = provide(AddPostUseCase)

