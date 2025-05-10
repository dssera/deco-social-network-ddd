from typing import Annotated 

from dishka import FromDishka
from dishka.integrations.fastapi import inject

from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes

from src.application.dtos.auth import UserDTO
from src.domain.auth.services.jwt_service import JwtService
from src.domain.auth.repositories.user_repository import UserRepository
from src.domain.auth.dtos import TokenData
from src.domain.auth.entities.user import User


# Token extraction marker for FastAPI Swagger UI.
# The actual token processing will be handled behind the Identity Provider.
oauth2_schema = OAuth2PasswordBearer(
    tokenUrl="/auth/token",
)

@inject
async def get_current_user(
        security_scopes: SecurityScopes,
        token: Annotated[str, Security(oauth2_schema)], 
        jwt_service: FromDishka[JwtService],  # ✅ FIXED
        user_repo: FromDishka[UserRepository],  # ✅ FIXED
) -> UserDTO:
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    print(token)
    token_data: TokenData = jwt_service.parse_token(token)
    user: User = await user_repo.get_one_or_none(username=token_data.username)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
    if token_data.roll not in security_scopes.scopes:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": authenticate_value},
        )
    return UserDTO.model_validate(user)