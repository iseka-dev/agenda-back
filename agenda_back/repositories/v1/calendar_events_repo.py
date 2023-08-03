"""Repository to query Calendar Events in postgres db."""

from agenda_back.db.models import CalendarEvent


def get_calendar_events() -> list[CalendarEvent]:
    """Get list of calendar events from database."""
