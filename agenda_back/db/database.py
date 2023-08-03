"""database implementation."""
from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from agenda_back.common.config import settings

engine = create_engine(settings.SQLITE_URL, echo=True)


def db_init() -> None:
    """Initialize db at server startup."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator:
    """Yield a session. It commits after all the code was run."""
    with Session(engine) as session:
        yield session
