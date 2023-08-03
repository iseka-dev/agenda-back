"""Service to handle calendar events."""

from agenda_back.db.models import CalendarEvent
from agenda_back.repositories.v1 import calendar_events_repo


class CalendarEventService:
    """Class to manage Calendar Events."""

    def get_calendar_events(self) -> list[
        CalendarEvent
    ]:
        """Get list of Calendar Events."""
        return calendar_events_repo.get_calendar_events()

    def create_calendar_event(self, calendar_event: CalendarEvent) -> str:
        """Create a calendar event."""
        return calendar_events_repo.create_calendar_event_repo(calendar_event)
