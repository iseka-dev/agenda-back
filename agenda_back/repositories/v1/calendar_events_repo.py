"""Repository to query Calendar Events in postgres db."""

import uuid

from sqlalchemy.orm import Session

from agenda_back.common.logger import log
from agenda_back.db.models import CalendarEvent
from agenda_back.schemas.v1.calendar_event_schemas import (
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


def create_calendar_event_repo(
    calendar_event: CalendarEvent,
    session: Session
) -> IdResponse:
    """Create a Calendar Event Object in the db."""
    log.info(f"Creating Calendar Event: {calendar_event}")

    new_calendar_event = CalendarEvent(
        id_=uuid.uuid4(),
        start_datetime="2023-08-08T00:00:00",
        end_datetime="2023-08-08T12:00:00",
        title="Calendar Event Title",
        description="Some Calendar Event description"
    )

    session.add(new_calendar_event)
    session.commit()
    session.refresh(new_calendar_event)

    log.info(f"Calendar Event stored in database: {new_calendar_event}")

    return {"id_": new_calendar_event.id_}
