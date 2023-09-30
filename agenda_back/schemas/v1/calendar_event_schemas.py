"""This module has Calendar Events reladted schemas for type validation."""
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CalendarEventSchema(BaseModel):
    """Base Schema Class for Calendar Events."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    start_datetime: datetime
    end_datetime: datetime
    title: str = "Event Title"
    description: str | None = "Missing description"
    owner_id: UUID
    attendee_ids: list[UUID] | None = None


class CalendarEventsPaginatedResponse(BaseModel):
    """Schema with an only field that returns a list of CalendarEventSchema."""

    calendar_events: list[CalendarEventSchema]
    total_count: int

class CalendarEventCreateRequest(BaseModel):
    """Base Schema Class for Calendar Events."""

    start_datetime: datetime
    end_datetime: datetime
    title: str = "Event Title"
    description: str | None = "Missing description"
    attendee_ids: list[UUID] = []
