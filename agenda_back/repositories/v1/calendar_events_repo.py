"""Repository to query Calendar Events in postgres db."""

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from agenda_back.common.logger import log
from agenda_back.db.models import CalendarEvent
from agenda_back.schemas.v1.calendar_event_schemas import (
    CalendarEventCreateRequest,
    CalendarEventSchema,
    CalendarEventsPaginatedResponse,
)
from agenda_back.schemas.v1.common_schemas import (
    IdOnlyResponse,
    PaginationSchema,
)


def get_calendar_events(
    session: Session,
    pagination: PaginationSchema
) -> CalendarEventsPaginatedResponse:
    """Get list of calendar events from database."""
    calendar_events = session.query(
        CalendarEvent
    ).offset(pagination.offset).limit(pagination.limit).order_by(
        pagination.order_by(pagination.sort)
    ).all()
    return CalendarEventsPaginatedResponse(
        calendar_events=calendar_events,
        total_count=len(calendar_events)
    )


def get_calendar_event(
    calendar_event_id: str,
    session: Session
) -> CalendarEventSchema:
    """Get list of calendar events from database."""
    query = select(CalendarEvent).where(CalendarEvent.id == calendar_event_id)
    calendar_event = session.scalar(
        query
    )
    return CalendarEventSchema(
        id=calendar_event.id,
        start_datetime=calendar_event.start_datetime,
        end_datetime=calendar_event.end_datetime,
        title=calendar_event.title,
        description=calendar_event.description
    )


def create_calendar_event(
    calendar_event: CalendarEventCreateRequest,
    session: Session
) -> IdOnlyResponse:
    """Create a Calendar Event Object in the db."""
    calendar_event = CalendarEvent(
        id=str(uuid.uuid4()),
        start_datetime=calendar_event.start_datetime,
        end_datetime=calendar_event.end_datetime,
        title=calendar_event.title,
        description=calendar_event.description
    )

    session.add(calendar_event)
    session.commit()
    session.refresh(calendar_event)

    log.info(f"Calendar Event stored in database: {calendar_event}")

    return IdOnlyResponse(id=calendar_event.id)
