from fastapi.security import OAuth2PasswordBearer

# Token extraction marker for FastAPI Swagger UI.
# The actual token processing will be handled behind the Identity Provider.
oauth2_schema = OAuth2PasswordBearer(
    tokenUrl="/auth/token",
)