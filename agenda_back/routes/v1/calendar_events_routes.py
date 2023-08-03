"""routes to access to the calendar events."""


from fastapi import APIRouter, HTTPException, status

from agenda_back.common.logger import log
from agenda_back.db.models import CalendarEvent
from agenda_back.models.v1.common_models import IdResponse
from agenda_back.services.v1.calendar_events_service import (
    CalendarEventService,
)

calendar_events_routes = APIRouter(
    prefix="/v1/calendar-events",
    tags=["calendar events"],
)


@calendar_events_routes.get("/", response_model=CalendarEvent)
async def get_calendar_events() -> CalendarEvent:
    """Public route to get list of calendar events."""
    try:
        return CalendarEventService().get_calendar_events()
    except Exception as e:
        log.error(f"Route Error: {e}")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"Error": "Calendar events are not available"},
    )


@calendar_events_routes.post("/", response_model=IdResponse)
async def create_calendar_event_route(
    calendar_event: CalendarEvent
) -> IdResponse:
    """Public route to get list of calendar events."""
    try:
        return CalendarEventService().create_calendar_event(calendar_event)
    except Exception as e:
        log.error(f"Route Error: {e}")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"Error": "Calendar events are not available"},
    )
