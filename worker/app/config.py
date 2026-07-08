import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/1")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://aiuser:changeme@localhost:5432/aiplatform",
    )
    CELERY_CONCURRENCY: str = os.getenv("CELERY_CONCURRENCY", "2")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    model_config = SettingsConfigDict(extra="ignore")


settings = Settings()
