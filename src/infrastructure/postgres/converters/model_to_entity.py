from uuid import UUID
from typing import List, Union


from src.domain.common.unit_of_work import UnitOfWork
from src.domain.pages.entities.page import Page
from src.domain.auth.entities.user import User
from src.domain.posts.entities.post import Post
from ..tables import (
    PageModel, 
    UserModel, 
    UserDataModel, 
    PostModel
    )

def model_to_page_entity(model: Union[PageModel, List[PageModel]], uow: UnitOfWork):
    def model_to_entity_single(model: PageModel, uow: UnitOfWork):
        print(model)
        return Page(
            id=model.id,
            uow=uow,
            name=model.name,
            about=model.about,
            is_private=model.is_private,
            user_id=model.user_id,
            unblock_date=model.unblock_date
        )
    if isinstance(model, list):
        return [model_to_entity_single(m, uow) for m in model]
    else:
        return model_to_entity_single(model, uow)

def model_to_post_entity(model: Union[PostModel, List[PostModel]], uow: UnitOfWork):
    def model_to_entity_single(model: PostModel, uow: UnitOfWork):
        return Post(
            id=model.id,
            uow=uow,
            title=model.title,
            body=model.body,
            created_at=model.created_at,
            page=model_to_page_entity(model.page, uow)
        )
    if isinstance(model, list):
        return [model_to_entity_single(m, uow) for m in model]
    else:
        return model_to_entity_single(model, uow)

def model_to_user_entity(
        user: UserModel, 
        user_data: UserDataModel, 
        uow: UnitOfWork
        ) -> User:
    return User(
        id=user.id,
        uow=uow,
        username=user.username,
        password=user.password,
        unblock_date=user.unblock_date,
        role=user.role,
        email=user_data.email,
        tg_nickname=user_data.tg_nickname
    )