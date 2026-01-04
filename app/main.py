from fastapi import FastAPI
from api.v1 import query
import time
import asyncio

app = FastAPI()

print("log")


@app.get("/")
def get_root():
    return {"Message": "Welcome to project akira"}


@app.get("/health")
async def check_health():
    time.sleep(2)  # DB Read
    return {"Message": "Server running"}


app.include_router(query.router, prefix="/api/v1")
