"""This module has the models for the project."""

import datetime
from uuid import UUID

from sqlmodel import Field, SQLModel


class CalendarEvent(SQLModel):
    """Calendar Events Base Class."""

    id_: UUID = Field(primary_key=True)
    day: int = Field()
    month: int = Field()
    start_date: datetime.date = Field()
    start_time: datetime.time = Field()
    start_datetime: datetime.datetime = Field()
    end_date: datetime.date = Field()
    end_time: datetime.time = Field()
    end_datetime: datetime.datetime = Field()
