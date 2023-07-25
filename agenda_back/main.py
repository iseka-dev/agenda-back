"""agenda App."""

from fastapi import FastAPI
from src.routes.base_routes import router

app = FastAPI()

app.include_router(router)
