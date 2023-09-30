"""Calendar events routes tests."""

from sqlite3 import IntegrityError
from unittest.mock import MagicMock, patch

from fastapi import status
from fastapi.testclient import TestClient

from agenda_back.common.logger import log
from agenda_back.schemas.v1.common_schemas import IdOnlyResponse
from agenda_back.schemas.v1.user_schemas import (
    CreateUserRequestSchema,
    UserSchema,
)

###########################################################
### CREATE USER TESTS                  #########
###########################################################


@patch(
    "agenda_back.services.v1.users_service.UserService."
    "create"
)
def test_calendar_routes_create_users_exception_mail_exists(
    m_service: MagicMock,
    client: TestClient,
    user_create_data: UserSchema
) -> None:
    """Test for create event route exception."""
    m_service.side_effect = IntegrityError("Error")
    response = client.post(
        "/v1/users/", json=user_create_data
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": {
            "Error": "Users Error: The email address was already taken."
        }
    }


@patch(
    "agenda_back.services.v1.users_service.UserService."
    "create"
)
def test_calendar_routes_create_users_exception(
    m_service: MagicMock,
    client: TestClient,
    user_create_data: UserSchema
) -> None:
    """Test for create event route exception."""
    m_service.side_effect = Exception("Error")
    response = client.post(
        "/v1/users/", json=user_create_data
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": {
            "Error": "Users Error: User was not created, please try again."
        }
    }


@patch(
    "agenda_back.services.v1.users_service.UserService."
    "create"
)
def test_user_routes_create_success(
    m_service: MagicMock,
    client: TestClient,
    user_create_data: CreateUserRequestSchema,
    id_uuid_data: IdOnlyResponse
) -> None:
    """Test for create User route."""
    m_service.return_value = id_uuid_data
    response = client.post(
        "/v1/users/",
        json=user_create_data
    )
    log.debug(f"{response.json()}")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"id": "a0866e45-9dd6-4874-b4b2-74efd20e5761"}
