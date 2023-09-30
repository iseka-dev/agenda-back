"""Calendar events routes tests."""

from unittest.mock import MagicMock, patch

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from agenda_back.common.logger import log
from agenda_back.schemas.v1.calendar_event_schemas import (
    CalendarEventCreateRequest,
    CalendarEventSchema,
    CalendarEventsPaginatedResponse,
)
from agenda_back.schemas.v1.common_schemas import IdOnlyResponse

###########################################################
### GET ALL CALENDAR EVENTS TESTS                  ########
###########################################################


@patch(
    "agenda_back.services.v1.calendar_events_service.CalendarEventService."
    "get_calendar_events"
)
def test_calendar_routes_get_calendar_events_exception(
    m_service: MagicMock, client: TestClient
) -> None:
    """Test for  GET method get_calendar_events. Exception."""
    m_service.side_effect = Exception("error")
    response = client.get("/v1/calendar-events/?offset=10")

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
    calendar_events_data: CalendarEventsPaginatedResponse
) -> None:
    """Test for  GET method get_calendar_events. Success."""
    m_service.return_value = calendar_events_data
    response = client.get("/v1/calendar-events/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == jsonable_encoder(calendar_events_data)


###########################################################
### GET CALENDAR EVENTS BY ID TESTS                #########
###########################################################


@patch(
    "agenda_back.services.v1.calendar_events_service.CalendarEventService."
    "get_calendar_event",
)
def test_calendar_routes_get_calendar_event_exception(
    m_service: MagicMock, client: TestClient
) -> None:
    """Test GET calendar event by id. Throws error."""
    m_service.side_effect = Exception("error")
    response = client.get(
        "/v1/calendar-events/832e350f-2689-4e02-83eb-c6e34b15885d"
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": {
            "Error": "Calendar event was not found. Please try again."
        }
    }


@patch(
    "agenda_back.services.v1.calendar_events_service.CalendarEventService."
    "get_calendar_event",
)
def test_calendar_routes_get_calendar_event_success(
    m_service: MagicMock,
    client: TestClient,
    calendar_event: CalendarEventSchema,
    id_uuid_string: str
) -> None:
    """Test GET calendar event by id. Returns calendar event successfully."""
    m_service.return_value = calendar_event
    response = client.get(
       f"/v1/calendar-events/{id_uuid_string}"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == jsonable_encoder(calendar_event)


###########################################################
### CREATE CALENDAR EVENTS TESTS                  #########
###########################################################


@patch(
    "agenda_back.services.v1.calendar_events_service.CalendarEventService."
    "create_calendar_event"
)
def test_calendar_routes_create_calendar_event_exception(
    m_service: MagicMock,
    client: TestClient,
    calendar_event_create_data: CalendarEventCreateRequest
) -> None:
    """Test for create event route exception."""
    m_service.side_effect = Exception("Error")
    response = client.post(
        "/v1/calendar-events/", json=calendar_event_create_data
        )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": {
            "Error": "[Error]: An unexpected error happened. Please try again."
        }
    }


@patch(
    "agenda_back.services.v1.calendar_events_service.CalendarEventService."
    "create_calendar_event"
)
def test_calendar_routes_create_calendar_event_success(
    m_service: MagicMock,
    client: TestClient,
    calendar_event_create_data: CalendarEventCreateRequest,
    id_uuid_data: IdOnlyResponse
) -> None:
    """Test for Create Calendar Event route."""
    m_service.return_value = id_uuid_data
    response = client.post(
        "/v1/calendar-events/",
        json=calendar_event_create_data
    )
    log.debug(f"{response.json()}")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"id": "a0866e45-9dd6-4874-b4b2-74efd20e5761"}
