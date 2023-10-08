"""Helpers related with authentication."""

from datetime import timedelta, utcnow

from jose import jwt
from passlib.context import CryptContext

from agenda_back.common.config import settings

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    """Get hashed version of user password."""
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    """Verify that introduced password corresponds with the stored one."""
    return password_context.verify(password, hashed_pass)


def create_token(
    payload: dict[str], expires_delta: int | None = None
) -> str:
    """Create token with expiration date."""
    if expires_delta is not None:
        expires_delta = utcnow() + expires_delta
    else:
        expires_delta = utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_MINUTES_VALIDITY_TIME
        )

    to_encode = {"exp": expires_delta, "sub": str(payload)}
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM
    )
    return encoded_jwt
