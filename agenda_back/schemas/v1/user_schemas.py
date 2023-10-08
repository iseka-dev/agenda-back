"""User Schemas."""

from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
)


class CreateUserRequestSchema(BaseModel):
    """Base Schema Class for Users."""

    username: str
    password: str
    email: str
    first_name: str
    second_name: str | None = None
    last_name: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "username": "admin",
                    "password": "admin123123",
                    "email": "admin@mail.com",
                    "first_name": "Juan",
                    "second_name": "Coso",
                    "last_name": "Perez",
                }
            ]
        }
    )

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
