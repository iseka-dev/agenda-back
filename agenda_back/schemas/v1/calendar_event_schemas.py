"""This module has Calendar Events reladted schemas for type validation."""
import datetime
import uuid

from pydantic import BaseModel, ConfigDict


class CalendarEventSchema(BaseModel):
    """Base Schema Class for Calendar Events."""

    model_config = ConfigDict(from_attributes=True)

    id_: uuid.UUID
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    title: str = "Event Title"
    description: str | None = "Missing description"


class CalendarEventsResponse(BaseModel):
    """Schema with an only field that returns a list of CalendarEventSchema."""

    calendar_events: list[CalendarEventSchema]


class CalendarEventCreateRequest(BaseModel):
    """Base Schema Class for Calendar Events."""

    model_config = ConfigDict(from_attributes=True)

    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    title: str = "Event Title"
    description: str | None = "Missing description"
