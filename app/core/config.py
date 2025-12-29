from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    pinecone_api: str
    pinecone_host: str
    pinecone_index: str
    default_character: str
    groq_api: str
    default_model: str


settings = Settings()
