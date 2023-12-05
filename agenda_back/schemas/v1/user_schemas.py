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
    first_name: str
    second_name: str | None = None
    last_name: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "username": "admin@mail.com",
                    "password": "admin123123",
                    "first_name": "Juan",
                    "second_name": "Coso",
                    "last_name": "Perez",
                }
            ]
        }
    )

class UserSchema(BaseModel):
    """Base Schema Class for Users."""

    id: UUID
    username: str
    password: str
    first_name: str
    second_name: str | None = None
    last_name: str

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    """Schema for a single User with no exposed password."""

    id: UUID
    username: str
    first_name: str
    second_name: str | None = None
    last_name: str


class UsersPaginatedDBResponse(BaseModel):
    """Users schema for db response. password included."""

    users: list[UserSchema]
    total_count: int

class UsersPaginatedResponse(BaseModel):
    """Users schema for db response. password excluded."""

    users: list[UserResponse]
    total_count: int

class CurrentUser(BaseModel):
    """Schema with the data about current api user."""

    expiration_time: int
    password: str | None
