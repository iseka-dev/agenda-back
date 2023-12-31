"""agenda App."""

from fastapi import FastAPI

from agenda_back.db.database import db_init
from agenda_back.routes.base_routes import router

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
def startup() -> None:
    """Execute at server startup."""
    db_init()


@app.on_event("shutdown")
def shutdown() -> None:
    """Execute at shutdown."""
