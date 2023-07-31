"""agenda App."""

from fastapi import FastAPI

from agenda_back.db import database
from agenda_back.routes.base_routes import router

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def on_startup() -> None:
    """Initialize database on server startup."""
    database.init_db()
