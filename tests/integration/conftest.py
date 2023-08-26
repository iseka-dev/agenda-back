"""Configurations for integrations tests."""
from collections.abc import Generator

from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

from agenda_back.db.database import Base, engine, get_db_session
from agenda_back.main import app

SQLALCHEMY_DATABASE_URL = "sqlite://"

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base.metadata.create_all(bind=engine)


def override_get_db() -> Generator:
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db_session] = override_get_db

client = TestClient(app)
