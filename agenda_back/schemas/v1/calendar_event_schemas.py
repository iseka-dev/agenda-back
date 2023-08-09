"""This module has Calendar Events reladted schemas for type validation."""
import datetime
import uuid

from pydantic import BaseModel


class CalendarEventBase(BaseModel):
    """Base Schema Class for Calendar Events."""

    id_: uuid.UUID
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    title: str
    description: str


class CalendarEventCreate(CalendarEventBase):
    """Schema class for Create Calendar Events Requests."""
