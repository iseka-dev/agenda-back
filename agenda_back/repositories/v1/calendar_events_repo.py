"""Repository to query Calendar Events in postgres db."""

from fastapi import Query
from sqlmodel import Depends, Session, select

from agenda_back.db.database import get_session
from agenda_back.db.models import CalendarEvent


def get_calendar_events(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
) -> list[CalendarEvent]:
    """Get list of calendar events from database."""
    CalendarEvent.from_orm()
    calendar_events = session.excec(
        select(CalendarEvent).offset(offset).limit(limit)
    ).all()
    return calendar_events
