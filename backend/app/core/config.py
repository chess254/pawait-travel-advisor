from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "PawaIt AI Travel Assistant API"
    VERSION: str = "1.1.0"
    GEMINI_API_KEY: str | None = None
    PORT: int = 8000
    DEBUG: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
