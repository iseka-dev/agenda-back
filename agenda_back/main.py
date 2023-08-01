"""agenda App."""

from fastapi import FastAPI

from agenda_back.routes.base_routes import router

app = FastAPI()

app.include_router(router)
