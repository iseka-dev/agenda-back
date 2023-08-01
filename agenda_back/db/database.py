"""database implementation."""


from sqlmodel import SQLModel, create_engine

from agenda_back.common.config import settings
from agenda_back.common.logger import log
from agenda_back.db import models

log.info(models)

engine = create_engine(settings.SQLITE_URL, echo=True)


def db_init() -> None:
    """Initialize db at server startup."""
    SQLModel.metadata.create_all(engine)
