from pinecone import PineconeAsyncio
from functools import lru_cache
import redis.asyncio as aioredis

from core.config import settings


@lru_cache
def get_pinecone_index():
    pc = PineconeAsyncio(settings.pinecone_api)
    return pc.IndexAsyncio(host=settings.pinecone_host)


def get_redis_client():
    pool = aioredis.ConnectionPool(
        host=settings.redis_host,
        port=16325,
        decode_responses=True,
        username="default",
        password=settings.redis_password,
    )

    return aioredis.Redis(connection_pool=pool)
