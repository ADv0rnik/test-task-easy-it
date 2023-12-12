import os
from pathlib import Path
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


BASE_DIR = (Path(__file__) / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    API_V1_STR: str = "/gpt/v1"
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PORT: int  # Use the name variable PORT for deploy to railway.app. Do not change it to another name!

    API_KEY: str

    ALLOWED_ORIGIN: list[AnyHttpUrl] = [
        'http://localhost',
        'http://127.0.0.1',
        'http://0.0.0.0'
    ]

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
