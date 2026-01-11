from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "postgresql+asyncpg://workout:workout@localhost:5432/workout"
    app_host: str = "127.0.0.1"
    app_port: int = 8000


settings = Settings()
