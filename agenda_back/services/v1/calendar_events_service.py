"""Service to handle calendar events."""

from agenda_back.db.models import CalendarEvent
from agenda_back.repositories.v1 import calendar_events_repo


class CalendarEventService:
    """Class to get images from OPEN AI."""

    def get_calendar_events(self) -> list[
        CalendarEvent
    ]:
        """Get hte list of Calendar Events."""
        return calendar_events_repo.get_calendar_events()
