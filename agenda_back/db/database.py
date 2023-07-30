"""Database settings."""

from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from agenda_back.common.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)


def init_db() -> None:
    """Database initialization."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session]:
    """Session for dependency injection."""
    with Session(engine) as session:
        yield session
