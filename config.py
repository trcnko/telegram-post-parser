from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    GOOGLE_SHEET_ID: str
    CREDENTIALS_FILE: str
    SHEET_NAME: str
    TARGET_HASHTAGS: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()