"""Repository to query Calendar Events in postgres db."""

import uuid

from sqlalchemy.orm import Session

from agenda_back.common.logger import log
from agenda_back.db.models import CalendarEvent
from agenda_back.schemas.v1.calendar_event_schemas import (
    CalendarEventCreateRequest,
    CalendarEventsResponse,
)
from agenda_back.schemas.v1.common_schemas import IdResponse


def get_calendar_events(
    session: Session,
    skip: int = 0,
    limit: int = 100
) -> list[CalendarEvent]:
    """Get list of calendar events from database."""
    calendar_events = session.query(
        CalendarEvent
    ).offset(skip).limit(limit).all()
    return CalendarEventsResponse(calendar_events=calendar_events)


def create_calendar_event(
    calendar_event: CalendarEventCreateRequest,
    session: Session
) -> IdResponse:
    """Create a Calendar Event Object in the db."""
    calendar_event = CalendarEvent(
        id_=uuid.uuid4(),
        start_datetime=calendar_event.start_datetime,
        end_datetime=calendar_event.end_datetime,
        title=calendar_event.title,
        description=calendar_event.description
    )

    session.add(calendar_event)

    log.info(f"Calendar Event stored in database: {calendar_event}")

    return IdResponse(id_=calendar_event.id_)
