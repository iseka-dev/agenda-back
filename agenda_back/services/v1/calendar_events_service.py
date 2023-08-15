"""Service to handle calendar events."""
from sqlalchemy.orm import Session

from agenda_back.repositories.v1 import calendar_events_repo
from agenda_back.schemas.v1.calendar_event_schemas import (
    CalendarEventSchema,
)
from agenda_back.schemas.v1.common_schemas import IdResponse


class CalendarEventService:
    """Class to manage Calendar Events."""

    def get_calendar_events(
        self, db_session: Session
    ) -> list[CalendarEventSchema]:
        """Get list of Calendar Events."""
        calendar_events = calendar_events_repo.get_calendar_events(db_session)
        return [
            CalendarEventSchema(
                id_=event.id_,
                start_datetime=event.start_datetime,
                end_datetime=event.end_datetime,
                title=event.title,
                description=event.description
            ) for event in calendar_events
        ]

    def create_calendar_event(
        self, calendar_event: CalendarEventSchema, db_session: Session
    ) -> IdResponse:
        """Create a calendar event."""
        return calendar_events_repo.create_calendar_event_repo(
            calendar_event, db_session
        )
