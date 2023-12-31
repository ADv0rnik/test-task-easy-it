import os
from pathlib import Path
from typing import List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


BASE_DIR = (Path(__file__) / ".." / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    API_V1_STR: str = "/gpt/v1"
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PORT: int

    API_KEY: str
    GIGA_KEY: str
    MODEL: str

    ALLOWED_ORIGIN: List[AnyHttpUrl] = [
        'http://localhost',
        'http://127.0.0.1',
        'http://0.0.0.0'
    ]

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(levelname)-7s %(asctime)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, 'logs', 'api.log'),
            "formatter": "standard",
            "encoding": "UTF-8",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 1000
        }
    },
    "loggers": {
        "easy_it": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        }
    }
}