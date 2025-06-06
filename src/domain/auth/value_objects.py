from enum import StrEnum


class RoleEnum(StrEnum):
    USER = "USER"
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"
    GUEST = "GUEST"