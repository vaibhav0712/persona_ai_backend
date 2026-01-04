from pinecone import PineconeAsyncio
from functools import lru_cache

from core.config import settings


@lru_cache
def get_pinecone_index():
    pc = PineconeAsyncio(settings.pinecone_api)
    # clean_host = settings.pinecone_host.replace('"', '').replace("'", "").replace("https://", "")

    return pc.IndexAsyncio(host=settings.pinecone_host)
