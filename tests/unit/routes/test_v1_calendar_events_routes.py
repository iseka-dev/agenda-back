"""Calendar events routes tests."""

from unittest.mock import MagicMock, patch

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from agenda_back.common.logger import log
from agenda_back.schemas.v1.calendar_event_schemas import (
    CalendarEventSchema,
    CalendarEventsResponse,
)
from agenda_back.schemas.v1.common_schemas import IdResponse


@patch(
    "agenda_back.services.v1.calendar_events_service.CalendarEventService."
    "get_calendar_events"
)
def test_calendar_routes_get_calendar_events_exception(
    m_service: MagicMock, client: TestClient
) -> None:
    """Test for home route."""
    m_service.side_effect = Exception("error")
    response = client.get("/v1/calendar-events/")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "detail": {
            "Error": "Calendar events are not available"
        }
    }


@patch(
    "agenda_back.services.v1.calendar_events_service.CalendarEventService."
    "get_calendar_events"
)
def test_calendar_routes_get_calendar_events_success(
    m_service: MagicMock,
    client: TestClient,
    calendar_events_data: CalendarEventsResponse
) -> None:
    """Test for home route."""
    m_service.return_value = calendar_events_data
    response = client.get("/v1/calendar-events/")
    log.debug(calendar_events_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == jsonable_encoder(calendar_events_data)


@patch(
    "agenda_back.services.v1.calendar_events_service.CalendarEventService."
    "create_calendar_event"
)
def test_calendar_routes_create_calendar_event_exception(
    m_service: MagicMock,
    client: TestClient,
    calendar_event_creation_data: CalendarEventSchema
) -> None:
    """Test for create event route exception."""
    m_service.side_effect = Exception("Error")
    response = client.post(
        "/v1/calendar-events/", json=calendar_event_creation_data
        )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": {
            "Error": "[RCE01]: An unexpected error happened. Please try again."
        }
    }


@patch(
    "agenda_back.services.v1.calendar_events_service.CalendarEventService."
    "create_calendar_event"
)
def test_calendar_routes_create_calendar_event_success(
    m_service: MagicMock,
    client: TestClient,
    calendar_event_creation_data: CalendarEventSchema,
    id_uuid_data: IdResponse
) -> None:
    """Test for Create Calendar Event route."""
    m_service.return_value = id_uuid_data
    response = client.post(
        "/v1/calendar-events/",
        json=calendar_event_creation_data
    )
    log.debug(f"{response.json()}")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"id_": "a0866e45-9dd6-4874-b4b2-74efd20e5761"}
