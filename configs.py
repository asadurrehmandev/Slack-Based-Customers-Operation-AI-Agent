from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    LLM_URL: str
    LLM_API_KEY: str

    SLACK_BOT_OPERATIONS_ASSISTANT_TOKEN: str
    SLACK_CHANNEL_ID: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
