"""Repository to query Calendar Events in postgres db."""


from sqlalchemy import select
from sqlalchemy.orm import Session

from agenda_back.common.logger import log
from agenda_back.db.models.calendar_event_models import CalendarEvent
from agenda_back.schemas.v1.calendar_event_schemas import (
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
    ).order_by(
        pagination.order_by(pagination.sort)
    ).offset(pagination.offset).limit(pagination.limit).all()
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
        description=calendar_event.description,
        owner_id=calendar_event.owner_id,
        attendee_ids=calendar_event.attendee_ids,
    )


def create_calendar_event(
    calendar_event: CalendarEventSchema,
    session: Session
) -> IdOnlyResponse:
    """Create a Calendar Event Object in the db."""
    calendar_event = CalendarEvent(
        id=str(calendar_event.id),
        start_datetime=calendar_event.start_datetime,
        end_datetime=calendar_event.end_datetime,
        title=calendar_event.title,
        owner_id=str(calendar_event.owner_id),
    )

    session.add(calendar_event)
    session.commit()
    session.refresh(calendar_event)

    log.info(f"Calendar Event stored in database: {calendar_event}")

    return IdOnlyResponse(id=calendar_event.id)
