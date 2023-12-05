"""This module has common schemas for type validation."""

from collections.abc import Callable
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    FieldValidationInfo,
    field_validator,
)

from agenda_back.common.config import settings
from agenda_back.common.enums import Orderby


class IdOnlyResponse(BaseModel):
    """ID only response schema."""

    id: UUID

    model_config = ConfigDict(from_attributes=True)


class PaginationSchema(BaseModel):
    """Pagination schema with skip and offset values."""

    offset: int = 0
    limit: int = 10
    sort: str = "id"
    order: str = "asc"

    model_config = ConfigDict(
        # TODO: validate_default as a way to
        # fullfull default values instead of classmethods.
        # TODO: validate_assignment=True,
        json_schema_extra={
            "examples": [
                {
                    "offset": 0,
                    "limit": 10,
                    "sort": "id",
                    "order": "asc",
                }
            ]
        }
    )

    @field_validator("*", mode="before")
    @classmethod
    def use_default_if_none(
        cls, v: str, field: FieldValidationInfo
    ) -> Callable:
        """Use default value if none."""
        if v is None:
            return cls.model_fields[f"{field.field_name}"].default
        return v

    @property
    def order_by(self) -> Orderby:
        """Order query results by selected field."""
        return Orderby.ASC if self.order.lower() == "asc" else Orderby.DESC

    @property
    def limit_page(self) -> int:
        """Set a maximum imit for an amount of item per page."""
        self.limit = (
            settings.PAGE_LIMIT
            if self.limit > settings.PAGE_LIMIT
            else self.limit
        )
        return self.limit
