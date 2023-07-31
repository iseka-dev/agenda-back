"""
This module has the main settings for a FastApi project.

Classes
-------
- Settings: Has the necessary settings for the project
"""

import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    This class has most settings for the project.

    It loads most vars from an env file.
    """

    load_dotenv()

    DATABASE_URL = os.getenv("DATABASE_URL", "")

    DB_USER = os.getenv("DB_USER", "")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_SERVER = os.getenv("DB_SERVER", "")
    DB_PORT = os.getenv("DB_PORT", "")
    DB_NAME = os.getenv("DB_NAME", "")
    DB_CONNECTION_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"

settings = Settings()
