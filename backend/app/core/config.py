"""Application settings loaded from environment variables / .env using Pydantic Settings (DATABASE_URL, JWT secrets, API keys, thresholds).

Belongs to: Module 1 Data Intake.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Typed settings object populated from the environment."""

    class Config:
        env_file = ".env"


settings = Settings()
