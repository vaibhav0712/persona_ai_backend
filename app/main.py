from dotenv import load_dotenv

load_dotenv()  # Only for Local development

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
import asyncio

from api.v1 import query

origins = [
    "https://projectakira.netlify.app",
    "http://localhost:5500",
    "http://localhost",
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

print("log")


@app.get("/")
def get_root():
    return {"Message": "Welcome to project akira"}


@app.get("/health")
async def check_health():
    time.sleep(2)  # DB Read
    return {"Message": "Server running"}


app.include_router(query.router, prefix="/api/v1")
