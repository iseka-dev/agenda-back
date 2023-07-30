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

settings = Settings()
