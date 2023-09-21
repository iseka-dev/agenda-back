"""This module has the models for the project."""

import datetime

from sqlalchemy import Column, DateTime, String, Text, Uuid

from agenda_back.db.database import Base

now = datetime.datetime.utcnow


class CalendarEvent(Base):
    """Calendar Events Base Class."""

    __tablename__ = "calendar_events"

    id_ = Column(Uuid, primary_key=True, index=True)
    create_datetime = Column(DateTime, default=now)
    last_update_datetime = Column(DateTime, default=now, onupdate=now)
    removed_datetime = Column(DateTime, default=None)

    start_datetime = Column(String)
    end_datetime = Column(String)

    title = Column(String, default="Calendar Event Title")
    description = Column(Text, default=None)
