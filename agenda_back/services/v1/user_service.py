"""Module with User service."""

from uuid import UUID, uuid4

from sqlalchemy.orm import Session

from agenda_back.repositories import users_repo
from agenda_back.schemas.v1.common_schemas import IdOnlyResponse
from agenda_back.schemas.v1.user_schemas import (
    CreateUserRequestSchema,
    UserSchema,
)


class UserService:
    """Service class for users features."""

    def create(
        self, data: CreateUserRequestSchema, session: Session
    ) -> IdOnlyResponse:
        """Create method for users."""
        user_data = data.model_dump()
        user_data["id"] = uuid4()
        user_data["owner_id"] = UUID("b3b020aa-f055-46d0-8100-35c0ab7e8b1d")
        user = UserSchema(**user_data)
        return users_repo.create_user(user, session)
