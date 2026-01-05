from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pinecone_api: str
    pinecone_host: str
    pinecone_index: str
    default_character: str
    groq_api: str
    default_model: str

    class Config:
        env_file = ".env"


settings = Settings()
