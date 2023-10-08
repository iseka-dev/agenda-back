"""
This module has the main settings for a FastApi project.

Classes
-------
- Settings: Has the necessary settings for the project
"""

import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    This class has most settings for the project.

    It loads most vars from an env file.
    """

    load_dotenv()

    # Database
    SQLITE_URL: str = os.getenv(
        "SQLITE_URL", ""
    )

    # Pagination
    PAGE_LIMIT: int = os.getenv(
        "PAGE_LIMIT", "100"
    )

    # Auth
    JWT_SECRET_KEY: str = os.getenv(
        "JWT_SECRET_KEY", ""
    )
    JWT_REFRESH_SECRET_KEY: str = os.getenv(
        "JWT_REFRESH_SECRET_KEY", ""
    )
    JWT_ALGORITHM: str = os.getenv(
        "JWT_ALGORITHM", ""
    )
    ACCESS_TOKEN_TTL_MINUTES: int = os.getenv(
        "ACCESS_TOKEN_TTL_MINUTES", "60"
    )


settings = Settings()
