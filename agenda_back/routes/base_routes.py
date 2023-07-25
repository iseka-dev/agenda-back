"""This module has the base routes for the project."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health-check", tags=["health-check"])
async def health_check() -> dict:
    """Check the online status of the package."""
    return {"check": {"server": "OK", "database": "OK"}}
