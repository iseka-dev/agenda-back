"""This module has common schemas for type validation."""

import uuid

from pydantic import BaseModel, ConfigDict


class IdResponse(BaseModel):
    """ID only response."""

    model_config = ConfigDict(from_attributes=True)

    id_: uuid.UUID
