"""This module has the models for the project."""

import datetime
from uuid import UUID

from sqlmodel import Field, SQLModel


class CalendarEventBase(SQLModel):
    """Calendar Events Base Class."""

    id_: UUID
    day: int
    month: int
    start_date: datetime.date
    start_datetime: datetime.datetime
    end_date: datetime.date
    end_datetime: datetime.datetime


class CalendarEvent(SQLModel, table=True):
    """Calendar Events Table Class."""

    id_: UUID = Field(primary_key=True)
    day: int = Field()
    month: int = Field()
    start_date: datetime.date = Field()
    start_datetime: datetime.datetime = Field()
    end_date: datetime.date = Field()
    end_datetime: datetime.datetime = Field()
