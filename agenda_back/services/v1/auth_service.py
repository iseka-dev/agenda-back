"""Auth service."""

from datetime import datetime, timedelta, timezone

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestFormStrict
from sqlalchemy.orm import Session

from agenda_back.common.config import settings
from agenda_back.common.enums import TokenTypes
from agenda_back.common.exceptions import InvalidCredentialsError
from agenda_back.helpers.auth_helpers import create_token, verify_password
from agenda_back.repositories import users_repo


class AuthService:
    """Service for user authentication."""

    def login(
        self,
        db_session: Session,
        data: OAuth2PasswordRequestFormStrict = Depends(),
    ) -> dict:
        """Login service."""
        user = users_repo.get_by_username(db_session, data.username)

        if not verify_password(data.password, user.password):
            message = "Incorrect email or password"
            raise InvalidCredentialsError(message)

        user_data = dict(user)
        user_data["expiration"] = (
            datetime.now(tz=timezone.utc)
            + timedelta(minutes=settings.JWT_TTL)
        )
        user_data["type"] = TokenTypes.AUTH
        token = create_token(user_data)

        refresh_ttl = (
            datetime.now(tz=timezone.utc)
            + timedelta(minutes=settings.JWT_REFRESH_TTL)
        )
        user_data["expiration"] = refresh_ttl
        user_data["type"] = TokenTypes.REFRESH
        refresh_token = create_token(user_data)

        return {"token": token, "refresh_token": refresh_token}
