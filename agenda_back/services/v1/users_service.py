"""Module with User service."""

from uuid import uuid4

from agenda_back.repositories.v1 import users_repo
from agenda_back.schemas.v1.common_schemas import IdOnlyResponse
from agenda_back.schemas.v1.user_schemas import (
    CreateUserRequestSchema,
    UserSchema,
)


class UserService:
    """Service class for users features."""

    def create(self, data: CreateUserRequestSchema) -> IdOnlyResponse:
        """Create method for users."""
        user_data = data.dict()
        user_data["id"] = uuid4()
        user = UserSchema(**user_data)
        return users_repo.create(user)
