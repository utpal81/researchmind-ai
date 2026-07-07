from pydantic_settings import BaseSettings, SettingsConfigDict




class Settings(BaseSettings):
    APP_NAME: str = "ResearchMind AI"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    EMBEDDING_MODEL: str = "BAAI/bge-base-en-v1.5"

    VECTOR_DB_PATH: str = "storage/vector_db"

    COLLECTION_NAME: str = "researchmind"

    GEMINI_API_KEY: str

    GEMINI_MODEL: str = "gemini-2.5-flash"
    

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()