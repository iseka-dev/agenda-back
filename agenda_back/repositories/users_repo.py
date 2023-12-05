"""Repository to query Calendar Events in postgres db."""

from uuid import UUID, uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from agenda_back.common.logger import log
from agenda_back.db.models.user_models import User
from agenda_back.schemas.v1.common_schemas import (
    IdOnlyResponse,
    PaginationSchema,
)
from agenda_back.schemas.v1.user_schemas import (
    CurrentUser,
    UserResponse,
    UserSchema,
    UsersPaginatedDBResponse,
    UsersPaginatedResponse,
)


def create_user(
    user: UserSchema,
    session: Session
) -> IdOnlyResponse:
    """Create a User Object the db."""
    user = User(
        id=str(uuid4()),
        username=user.username,
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


def get_users(
    pagination: PaginationSchema,
    session: Session
) -> UsersPaginatedResponse:
    """Get a list of users."""
    users = session.query(
        User
    ).offset(pagination.offset).limit(pagination.limit).order_by(
        pagination.order_by(pagination.sort)
    ).all()
    return UsersPaginatedDBResponse(
        users=users,
        total_count=len(users)
    )


def get_by_id(user_id: UUID, session: Session) -> UserSchema:
    """Get a single user by its id."""
    query = select(User).where(User.id == user_id)
    user = session.scalar(
        query
    )
    return UserResponse(user)


def get_by_username(session: Session, username: str) -> CurrentUser:
    """Get a user by its username."""
    query = select(User).where(User.username == username)
    user = session.execute(query).one().first()
    return UserResponse(
        id=user.id,
        username=user.username,
        first_name=user.first_name,
        second_name=user.second_name,
        last_name=user.last_name,
    )
