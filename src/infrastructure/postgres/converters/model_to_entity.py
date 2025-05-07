from uuid import UUID
from typing import List, Union


from src.domain.common.unit_of_work import UnitOfWork
from src.domain.pages.entities.page import Page
from src.domain.auth.entities.user import User
from ..tables import PageModel, UserModel, UserDataModel

def model_to_page_entity(model: Union[PageModel, List[PageModel]], uow: UnitOfWork):
    if isinstance(model, list):
        return [__model_to_page_entity_single(m, uow) for m in model]
    else:
        return __model_to_page_entity_single(model, uow)

def __model_to_page_entity_single(model: PageModel, uow: UnitOfWork):
    print(model)
    return Page(
        page_id=model.id,
        uow=uow,
        name=model.name,
        about=model.about,
        is_private=model.is_private,
        user_id=model.user_id,
        unblock_date=model.unblock_date
    )

def model_to_user_entity(
        user: UserModel, 
        user_data: UserDataModel, 
        uow: UnitOfWork
        ) -> User:
    return User(
        user_id=user.id,
        uow=uow,
        username=user.username,
        password=user.password,
        unblock_date=user.unblock_date,
        role=user.roll,
        email=user_data.email,
        tg_nickname=user_data.tg_nickname
    )