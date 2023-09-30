"""User Schemas."""

from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
)


class CreateUserRequestSchema(BaseModel):
    """Base Schema Class for Users."""

    model_config = ConfigDict(from_attributes=True)

    username: str
    password: str
    email: str
    first_name: str
    second_name: str | None = None
    last_name: str

class UserSchema(BaseModel):
    """Base Schema Class for Users."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str
    password: str
    email: str
    first_name: str
    second_name: str | None = None
    last_name: str
