from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    database_url: str = "postgresql+psycopg://ssbprep:ssbprep@localhost:5432/ssbprep"
    ingest_key: str = "change-me-local-only"
    jwt_secret: str = "change-me-local-only"
    jwt_access_ttl_seconds: int = 900
    jwt_refresh_ttl_seconds: int = 1_209_600


def get_settings() -> Settings:
    return Settings()
