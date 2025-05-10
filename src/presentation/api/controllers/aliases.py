from typing import Annotated

from fastapi import Security

from src.application.dtos.auth import UserDTO
from src.domain.auth.value_objects import RoleEnum
from ...common.fastapi_dependencies import get_current_user


security_user_annotation = Annotated[UserDTO, Security(get_current_user, scopes=[RoleEnum.USER])]