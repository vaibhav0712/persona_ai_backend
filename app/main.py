from dotenv import load_dotenv

load_dotenv()  # Local Only

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import time
import redis

from api.v1 import query
from db.connection import get_redis_client


origins = [
    "https://projectakira.netlify.app",
    "http://127.0.0.1:5500",
]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis_client = get_redis_client()


@app.middleware("http")
async def rate_limit(request: Request, call_next):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"

    try:
        request_count = await redis_client.get(key)
        print("client", client_ip, "count", request_count)

        if request_count and int(request_count) > 3:
            return JSONResponse(
                status_code=429, content={"detail": "Too many request. slow down"}
            )

        async with redis_client.pipeline() as pipe:
            pipe.incr(key)  # auto set counter

            if request_count is None:
                pipe.expire(key, 10)

            await pipe.execute()

    except redis.exceptions.ConnectionError:
        print("Redis connection failed, skipping rate limit check.")
        pass

    response = await call_next(request)
    return response


@app.get("/")
def get_root(request: Request):
    print("--- hit root ---")
    return {"Message": "Welcome to project akira"}


@app.get("/health")
async def check_health():
    time.sleep(2)  # DB Read
    return {"Message": "Server running"}


app.include_router(query.router, prefix="/api/v1")
