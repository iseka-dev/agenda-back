"""This module has the calendar_events models for the project."""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import TIMESTAMP, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from agenda_back.db.database import Base


class CalendarEvent(Base):
    """Calendar Events Base Class."""

    __tablename__ = "calendar_events"

    id: Mapped[str] = mapped_column(
        Text,
        primary_key=True,
        index=True,
        nullable=False,
        default=uuid4,
    )

    start_datetime: Mapped[str] = mapped_column(
        DateTime,
        nullable=False,
        index=True,
    )
    end_datetime: Mapped[str] = mapped_column(
        DateTime,
        index=True,
        nullable=False,
    )
    title: Mapped[str] = mapped_column(
        String(100),
        default="Calendar Event Title"
    )
    description: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
        default="Insert your description",
    )
    owner_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
    attendee_ids: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
        default=None
    )

    created_datetime: Mapped[str] = mapped_column(
        TIMESTAMP,
        default=datetime.utcnow,
    )
    last_update_datetime: Mapped[str] = mapped_column(
        TIMESTAMP,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    removed_datetime: Mapped[str] = mapped_column(
        TIMESTAMP,
        nullable=True,
        default=None
    )
