
"""Tests for calendar events service."""
from unittest.mock import MagicMock, patch

from agenda_back.schemas.v1.calendar_event_schemas import (
    CalendarEventCreateRequest,
    CalendarEventSchema,
)
from agenda_back.schemas.v1.common_schemas import IdOnlyResponse
from agenda_back.services.v1.calendar_events_service import (
    CalendarEventService,
)


@patch("agenda_back.repositories.v1.calendar_events_repo.get_calendar_events")
def test_calendar_events_service_get_calendar_events_sucess_empty_response(
    mocked_repo: MagicMock
) -> None:
    """
    Test for get_calendar_events method at Calendar Event service.

    Empty response success case.
    """
    mocked_repo.return_value = []
    expected = []
    session = MagicMock
    pagination = MagicMock
    result = CalendarEventService().get_calendar_events(session, pagination)

    assert result == expected


@patch("agenda_back.repositories.v1.calendar_events_repo.get_calendar_events")
def test_calendar_events_service_get_calendar_events_success(
    mocked_repo: MagicMock,
    calendar_events_data: MagicMock
) -> None:
    """
    Test for get_calendar_events method at Calendar Event service.

    Success case.
    """
    mocked_repo.return_value = calendar_events_data
    session = MagicMock
    pagination = MagicMock
    result = CalendarEventService().get_calendar_events(session, pagination)

    assert result == calendar_events_data


@patch("agenda_back.repositories.v1.calendar_events_repo.get_calendar_event")
def test_calendar_events_service_get_calendar_event_success(
    mocked_repo: MagicMock,
    calendar_event: CalendarEventSchema,
    id_uuid_string: str
) -> None:
    """
    Test for get_calendar_events method at Calendar Event service.

    Success case.
    """
    mocked_repo.return_value = calendar_event
    session = MagicMock
    result = CalendarEventService().get_calendar_event(session, id_uuid_string)

    assert result == calendar_event


@patch(
    "agenda_back.repositories.v1.calendar_events_repo.create_calendar_event"
)
def test_calendar_events_service_create_calendar_events_success(
    mocked_repo: MagicMock,
    id_uuid_data: IdOnlyResponse,
    calendar_event_create_data: CalendarEventCreateRequest
) -> None:
    """
    Test for get_calendar_events method at Calendar Event service.

    Success case.
    """
    mocked_repo.return_value = id_uuid_data
    session = MagicMock
    result = CalendarEventService().create_calendar_event(
        calendar_event_create_data, session
    )

    assert result == id_uuid_data
