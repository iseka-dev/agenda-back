"""Repository to query Calendar Events in postgres db."""

from fastapi import Depends, Query
from sqlmodel import Session, select

from agenda_back.db.database import get_session
from agenda_back.db.models import CalendarEvent
from agenda_back.models.v1.common_models import IdResponse


async def get_calendar_events(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
) -> list[CalendarEvent]:
    """Get list of calendar events from database."""
    CalendarEvent.from_orm()
    calendar_events = await session.exec(
        select(CalendarEvent).offset(offset).limit(limit)
    ).all()
    return calendar_events


async def create_calendar_event_repo(
    calendar_event: CalendarEvent,
    session: Session = Depends(get_session),
) -> IdResponse:
    """Create a Calendar Event Object in the db."""
    response = await session.add(CalendarEvent.from_orm(calendar_event))
    return response
