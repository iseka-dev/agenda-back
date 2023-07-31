"""Settings for postgres async db."""


import sqlalchemy
from sqlalchemy import create_engine
from src.settings import settings

from .database import Database

routes = {
    "default": {
        "host": settings.DB_SERVER,
        "user": settings.DB_USER,
        "password": settings.DB_PASSWORD,
        "name": settings.DB_NAME,
        "port": settings.DB_PORT,
    },
}

engine = create_engine(settings.DB_CONNECTION_URI, pool_pre_ping=True)
database = Database(routes)
metadata = sqlalchemy.MetaData()
