"""This module has common schemas for type validation."""

from uuid import UUID

from sqlmodel import SQLModel


class IdResponse(SQLModel):
    """ID only response."""

    id_: UUID
