import os
from dotenv import load_dotenv
from pydantic import BaseConfig

load_dotenv()


class GlobalConfig:
    def __init__(self):
        pass

    title: str = os.environ.get("TITLE", "FastAPI")
    version: str = "1.0.0"
    description: str = os.environ.get("DESCRIPTION", "")
    openapi_prefix: str = os.environ.get("OPENAPI_PREFIX", "")
    dock_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"
    api_prefix: str = "/api"

    postgres_user: str = os.environ.get("POSTGRES_USER", "postgres")
    postgres_password: str = os.environ.get("POSTGRES_PASSWORD", "postgres")
    postgres_db: str = os.environ.get("POSTGRES_DB", "postgres")
    postgres_host: str = os.environ.get("POSTGRES_HOST", "localhost")
    postgres_port: int = os.environ.get("POSTGRES_PORT", 5432)

    @property
    def sync_database_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
    
    @property
    def async_database_url(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

settings = GlobalConfig()
