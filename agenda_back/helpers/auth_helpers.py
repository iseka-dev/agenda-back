"""Helpers related with authentication."""


from jose import jwt
from passlib.context import CryptContext

from agenda_back.common.config import settings
from agenda_back.common.enums import TokenTypes
from agenda_back.common.exceptions import TokenTypeError

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    """Get hashed version of user password."""
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    """Verify that introduced password corresponds with the stored one."""
    return password_context.verify(password, hashed_pass)


def create_token(
    payload: dict[str]
) -> str:
    """Create token with expiration date."""
    encoded_jwt = jwt.encode(
        payload, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM
    )
    return encoded_jwt


def validate_token_type(required_type: TokenTypes, token_type: str) -> None:
    """
    Validate that the token is proper type.

    Possible types:
    AUTH | REFRESH | PASSWORD_CREATE | PASSWORD_RESET
    """
    try:
        token_type = TokenTypes(token_type)
    except Exception:
        msg = f"Invalid token type: '{token_type}'."
        raise TokenTypeError(msg)  # noqa: B904, TRY200
    if token_type != required_type:
        msg = f"""
            Required token type:'{required_type}'\n`
            Given token type: '{token_type}'.
        """
        raise TokenTypeError(msg)
