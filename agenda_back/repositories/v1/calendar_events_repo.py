"""Repository to query Calendar Events in postgres db."""

import uuid

from sqlalchemy.orm import Session

from agenda_back.common.logger import log
from agenda_back.db.models import CalendarEvent
from agenda_back.schemas.v1.common_schemas import IdResponse


async def get_calendar_events(
    session: Session,
    skip: int = 0,
    limit: int = 100
) -> list[CalendarEvent]:
    """Get list of calendar events from database."""
    CalendarEvent.from_orm()
    calendar_events = session.query(
        CalendarEvent
    ).offset(skip).limit(limit).all()
    return calendar_events


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
    )
    session.add(new_calendar_event)
    session.commit()
    session.refresh(new_calendar_event)
    log.info(f"Calendar Event stored in database: {new_calendar_event}")
    return {"id_": new_calendar_event.id_}
