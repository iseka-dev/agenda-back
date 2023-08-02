"""This module has the models for the project."""

from uuid import UUID

from sqlmodel import Field, SQLModel


class CalendarEventBase(SQLModel):
    """Calendar Events Base Class."""

    id_: UUID
    day: int
    month: int


class CalendarEvent(SQLModel, table=True):
    """Calendar Events Table Class."""

    id_: UUID = Field(primary_key=True)
    day: int = Field()
    month: int = Field()
