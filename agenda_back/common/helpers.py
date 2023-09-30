"""This module has the helpers for the project."""

from uuid import UUID, uuid4


def get_current_user_id() -> UUID:
    """
    Function to return current user id.

    Currently mocked.
    TODO: Pull user from request authentication.
    """  # noqa: D401
    return str(uuid4())
