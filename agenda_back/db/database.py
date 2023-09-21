"""database implementation."""
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from agenda_back.common.config import settings
from agenda_back.common.logger import log

engine = create_engine(
    settings.SQLITE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def db_init() -> None:
    """Initialize database."""
    log.info("Initializing database...")
    Base.metadata.create_all(bind=engine)
    log.info("The database has been initialized.")


def get_db_session() -> Generator:
    """Dependency to yield a session."""
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
