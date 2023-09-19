"""Dependencies for dependency injection in routes module."""

from fastapi import Request

from agenda_back.schemas.v1.common_schemas import PaginationSchema


def paginate(req: Request) -> PaginationSchema:
    """Dependency for requested data pagination."""
    return PaginationSchema(
        offset=req.query_params.get("offset"),
        limit=req.query_params.get("limit"),
        sort=req.query_params.get("sort"),
        order=req.query_params.get("order")
    )
