"""Enums used in calendar events app."""

from enum import Enum

from sqlalchemy import asc, desc


class BaseEnum(str, Enum):
    """Enum class extension for indexable or orderable enums."""

    @classmethod
    def index(cls, member: Enum) -> int:
        """Get index of enumerable element."""
        return list(cls).index(member)

    @classmethod
    def get(cls, index: int) -> Enum | None:
        """Get enumerable element by id."""
        elements = list(cls)
        if not isinstance(index, int) or index < 0 or index >= len(elements):
            return None
        return elements[index]


class Orderby(Enum):
    """Ordering enumeration."""

    ASC = asc
    DESC = desc
