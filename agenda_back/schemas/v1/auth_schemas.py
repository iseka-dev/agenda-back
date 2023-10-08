"""Authentication and authorization schemas."""

from pydantic import BaseModel, ConfigDict, EmailStr, field_validator

from agenda_back.schemas.v1.validator import ValidatorSchema


class Token(BaseModel):
    """Token schema."""

    token_type: str
    access_token: str


class TokenData(BaseModel):
    """Data to be used for tokenization."""

    username: str


class LoginSchema(BaseModel):
    """Schema to be used for a user at login."""

    username: EmailStr
    password: str


class SetPasswordRequestSchema(ValidatorSchema):
    """Schema to be used when setting a password for the first time."""

    password: str
    token: str

    model_config = ConfigDict(
        ExtraValues = "forbid"
    )

    @field_validator("*", mode="before")
    @classmethod
    def required_field(cls, value: str) -> str:
        """Check that require field has input."""
        return super().required_field(value)

    @field_validator("password", mode="before")
    @classmethod
    def password_validation(cls, value: str) -> str:
        """Validate that introduce password satisfies minimum conditions."""
        return super().password_validation(value)


class ResetPasswordRequestSchema(BaseModel):
    """Schema to be used when request a new password."""

    email: EmailStr

    model_config = ConfigDict(
        ExtraValues = "forbid"
    )
