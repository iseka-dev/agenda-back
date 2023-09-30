"""Repository to query Calendar Events in postgres db."""

from uuid import uuid4

from sqlalchemy.orm import Session

from agenda_back.common.logger import log
from agenda_back.db.models.user_models import User
from agenda_back.schemas.v1.common_schemas import (
    IdOnlyResponse,
)
from agenda_back.schemas.v1.user_schemas import (
    UserSchema,
)


def create_user(
    user: UserSchema,
    session: Session
) -> IdOnlyResponse:
    """Create a User Object the db."""
    user = User(
        id=str(uuid4()),
        username=user.username,
        email=user.email,
        password=user.password,
        first_name=user.first_name,
        second_name=user.second_name,
        last_name=user.last_name,
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    log.info(f"User stored in database: {user}")

    return IdOnlyResponse(id=user.id)
