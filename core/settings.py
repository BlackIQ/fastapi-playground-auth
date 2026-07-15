# Pydantic Settings
from pydantic_settings import BaseSettings, SettingsConfigDict


# Class settings
class Settings(BaseSettings):
    postgres_url: str = ""

    model_config = SettingsConfigDict(env_file="../.env")


# Run settings
settings = Settings()
