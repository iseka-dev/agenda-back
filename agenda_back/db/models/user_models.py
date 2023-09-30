"""This module has the user models for the project."""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from agenda_back.db.database import Base


class User(Base):
    """User Base Class."""

    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        Text,
        primary_key=True,
        index=True,
        default=uuid4(),
    )

    username: Mapped[str] = mapped_column(
        String(50),
        index=True,
        nullable=False
    )
    password: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    second_name: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )
    last_name: Mapped[str] = mapped_column(
        String(50),
        index=True,
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(50),
        index=True,
        nullable=False
    )

    create_datetime: Mapped[str] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    last_update_datetime: Mapped[str] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    removed_datetime: Mapped[str] = mapped_column(
        DateTime,
        default=None,
        nullable=True
    )
