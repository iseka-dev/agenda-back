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
    """Create a Calendar Event Object in the db."""
    user = User(
        id=str(uuid4()),
        start_datetime=user.start_datetime,
        end_datetime=user.end_datetime,
        title=user.title,
        description=user.description,
        owner=user.owner,
        attendees=[]
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    log.info(f"Calendar Event stored in database: {user}")

    return IdOnlyResponse(id=user.id)
