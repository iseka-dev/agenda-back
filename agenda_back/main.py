"""agenda App."""

from fastapi import FastAPI

from agenda_back.db.database import db_init
from agenda_back.routes.base_routes import router

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
def on_startup() -> None:
    """Initialize db at server startup."""
    db_init()
