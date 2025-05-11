from uuid import UUID
from typing import List, Union

from src.domain.pages.entities.page import Page
from src.domain.posts.entities.post import Post
from src.domain.auth.entities.user import User
from src.domain.common.unit_of_work import UnitOfWork

def page_entity_to_dict(entity: Union[Page, List[Page]]):
    def entity_to_dict_single(entity: Page):
        return {
            "id": entity.id,
            "name": entity.name,
            "about": entity.about,
            "is_private": entity.is_private,
            "user_id": entity.user_id,
            "unblock_date": entity.unblock_date
        }
            
    if isinstance(entity, list):
        return [entity_to_dict_single(m) for m in entity]
    else:
        return entity_to_dict_single(entity)
    

def post_entity_to_dict(entity: Union[Post, List[Post]]):
    def entity_to_dict_single(entity: Post):
        return {
            "id": entity.id,
            "title": entity.title,
            "body": entity.body,
            "created_at": entity.created_at,
            "page_id": entity.page_id,
        }
            
    if isinstance(entity, list):
        return [entity_to_dict_single(m) for m in entity]
    else:
        return entity_to_dict_single(entity)
    

def user_entity_to_dict(entity: Union[User, List[User]]):
    def entity_to_dict_single(entity: User):
        return {
            "id": entity.id,
            "username": entity.username,
            "password": entity.password,
            "unblock_date": entity.unblock_date,
            "role": entity.role,
            # "email": entity.email,
            # "tg_nickname": entity.tg_nickname
        }
            
    if isinstance(entity, list):
        return [entity_to_dict_single(m) for m in entity]
    else:
        return entity_to_dict_single(entity)