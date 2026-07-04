from pydantic_settings import BaseSettings, SettingsConfigDict


EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
class Settings(BaseSettings):
    APP_NAME: str = "ResearchMind AI"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()