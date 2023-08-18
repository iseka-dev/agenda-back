"""routes to access to the calendar events."""


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from agenda_back.common.logger import log
from agenda_back.db.database import get_db_session
from agenda_back.schemas.v1.calendar_event_schemas import (
    CalendarEventSchema,
    CalendarEventsResponse,
)
from agenda_back.schemas.v1.common_schemas import IdResponse
from agenda_back.services.v1.calendar_events_service import (
    CalendarEventService,
)

calendar_events_routes = APIRouter(
    prefix="/v1/calendar-events",
    tags=["calendar events"],
)


@calendar_events_routes.get(
    "/",
    response_model=CalendarEventsResponse,
    status_code=status.HTTP_200_OK
)
def get_calendar_events(
    db_session: Session = Depends(get_db_session)
) -> CalendarEventsResponse:
    """Public route to get list of calendar events."""
    try:
        return CalendarEventService().get_calendar_events(
            db_session
        )
    except Exception as e:
        log.error(f"Route Error: {e}")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"Error": "Calendar events are not available"},
    )


@calendar_events_routes.post(
    "/",
    response_model=IdResponse,
    status_code=status.HTTP_201_CREATED
)
def create_calendar_event(
    calendar_event: CalendarEventSchema,
    db_session: Session = Depends(get_db_session)
) -> IdResponse:
    """Public route to get list of calendar events."""
    try:
        return CalendarEventService(
        ).create_calendar_event(calendar_event, db_session)
    except Exception as e:
        log.error(f"Route Error: {e}")
        error = "[RCE01]: An unexpected error happened. Please try again."
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={"Error": error},
    )
