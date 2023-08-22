
"""Tests for calendar events service."""
from unittest.mock import MagicMock, patch

import pytest

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
    result = CalendarEventService().get_calendar_events(session)

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
    result = CalendarEventService().get_calendar_events(session)

    assert result == calendar_events_data


def test_calendar_events_service_create_calendar_events_missing_arguments(
) -> None:
    """
    Test for get_calendar_events method at Calendar Event service.

    Empty response success case.
    """
    session = MagicMock()
    with pytest.raises(Exception) as e:  # noqa: PT011
        CalendarEventService().create_calendar_event(
            db_session=session
        )

    assert str(e.value) == (
        "CalendarEventService.create_calendar_event() "
        "missing 1 required positional argument: 'calendar_event'"
    )
