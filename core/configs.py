from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # DATABASE CONFIGS
    DATABASE_HOST: str
    DATABASE_PORT: str

    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    # LLM CONFIGS
    LLM_URL: str
    LLM_API_KEY: str

    # SLACK CONFIGS
    SLACK_BOT_OPERATIONS_ASSISTANT_TOKEN: str
    SLACK_CHANNEL_ID: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
    )

    @computed_field
    @property
    def DATABASE_URI(self) -> str:
        return (
            f"postgresql://{self.DATABASE_USER}:"
            f"{self.DATABASE_PASSWORD}@"
            f"{self.DATABASE_HOST}:"
            f"{self.DATABASE_PORT}/"
            f"{self.DATABASE_NAME}"
        )


settings = Settings()
