"""Service to handle calendar events."""
from sqlalchemy.orm import Session

from agenda_back.repositories.v1 import calendar_events_repo
from agenda_back.schemas.v1.calendar_event_schemas import (
    CalendarEventSchema,
    CalendarEventsResponse,
)
from agenda_back.schemas.v1.common_schemas import IdResponse


class CalendarEventService:
    """Class to manage Calendar Events."""

    def get_calendar_events(
        self, db_session: Session
    ) -> CalendarEventsResponse:
        """Get list of Calendar Events."""
        return calendar_events_repo.get_calendar_events(db_session)

    def create_calendar_event(
        self, calendar_event: CalendarEventSchema, db_session: Session
    ) -> IdResponse:
        """Create a calendar event."""
        return calendar_events_repo.create_calendar_event_repo(
            calendar_event, db_session
        )
