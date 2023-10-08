"""Test for home route."""

from fastapi import APIRouter

from agenda_back.routes.v1.auth_routes import auth_routes
from agenda_back.routes.v1.calendar_events_routes import calendar_events_routes
from agenda_back.routes.v1.users_routes import users_routes

router = APIRouter()


@router.get("/", tags=["home"])
async def home() -> dict:
    """Agendapp Home address."""
    return {"Message": "Agendapp"}


@router.get("/health-check", tags=["health-check"])
async def health_check() -> dict:
    """Check the online status of the package."""
    return {"check": {"server": "OK", "database": "OK"}}

router.include_router(auth_routes)
router.include_router(calendar_events_routes)
router.include_router(users_routes)
