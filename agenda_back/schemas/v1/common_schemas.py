"""This module has common schemas for type validation."""

import uuid

from pydantic import BaseModel


class IdResponse(BaseModel):
    """ID only response."""

    id_: uuid.UUID

    class Config:
        """Config class for IdResponse Schema."""

        from_attributes = True
