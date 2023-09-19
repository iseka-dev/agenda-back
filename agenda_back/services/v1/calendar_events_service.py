"""Service to handle calendar events."""
from sqlalchemy.orm import Session

from agenda_back.repositories.v1 import calendar_events_repo
from agenda_back.schemas.v1.calendar_event_schemas import (
    CalendarEventCreateRequest,
    CalendarEventSchema,
    CalendarEventsPaginatedResponse,
)
from agenda_back.schemas.v1.common_schemas import (
    IdOnlyResponse,
    PaginationSchema,
)


class CalendarEventService:
    """Class to manage Calendar Events."""

    def get_calendar_events(
        self, db_session: Session, pagination: PaginationSchema
    ) -> CalendarEventsPaginatedResponse:
        """Get list of Calendar Events."""
        return calendar_events_repo.get_calendar_events(db_session, pagination)

    def get_calendar_event(
        self, calendar_event_id: str, session: Session
    ) -> CalendarEventSchema:
        """Get a single Calendar event, looging by id."""
        return calendar_events_repo.get_calendar_event(
            calendar_event_id, session
        )

    def create_calendar_event(
        self, calendar_event: CalendarEventCreateRequest, db_session: Session
    ) -> IdOnlyResponse:
        """Create a calendar event."""
        return calendar_events_repo.create_calendar_event(
            calendar_event, db_session
        )
