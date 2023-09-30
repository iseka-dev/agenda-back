"""Tests for calendar events service."""

from unittest.mock import MagicMock, patch

from agenda_back.schemas.v1.common_schemas import IdOnlyResponse
from agenda_back.schemas.v1.user_schemas import CreateUserRequestSchema
from agenda_back.services.v1.users_service import UserService


@patch(
    "agenda_back.repositories.v1.users_repo.create_user"
)
def test_users_service_create_users_success(
    mocked_repo: MagicMock,
    id_uuid_data: IdOnlyResponse,
    user_create_schema: CreateUserRequestSchema
) -> None:
    """
    Test for create method at Users service.

    Success case.
    """
    mocked_repo.return_value = id_uuid_data
    session = MagicMock
    result = UserService().create(
        user_create_schema, session
    )

    assert result == id_uuid_data
