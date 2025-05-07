from fastapi import HTTPException, status


jwt_is_expired_exc = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="JWT token is expired.",
                headers={"WWW-Authenticate": "Bearer"},
        )

wrong_jwt_token_exc = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Wrong refresh token. Please update page.",
                headers={"WWW-Authenticate": "Bearer"},
        )