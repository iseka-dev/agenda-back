"""This module has common schemas for type validation."""

import uuid
from collections.abc import Callable

from pydantic import (
    BaseModel,
    ConfigDict,
    FieldValidationInfo,
    field_validator,
)


class IdOnlyResponse(BaseModel):
    """ID only response schema."""

    model_config = ConfigDict(from_attributes=True)

    id_: uuid.UUID


class PaginationSchema(BaseModel):
    """Pagination schema with skip and offset values."""

    model_config = ConfigDict(
        json_schema_extra={
            "offset": 0,
            "limit": 10,
            "sort": "id",
            "order": "asc",
        }
    )

    offset: int = 0
    limit: int = 10
    sort: str = "id_"
    order: str = "asc"

    @field_validator("*", mode="before")
    @classmethod
    def use_default_if_none(
        cls, v: str, field: FieldValidationInfo
    ) -> Callable:
        """Use default value if none."""
        if v is None:
            return cls.model_config["json_schema_extra"][f"{field.field_name}"]
        return v
