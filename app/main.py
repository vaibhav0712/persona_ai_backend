from fastapi import FastAPI
from api.v1 import query

app = FastAPI()


@app.get("/")
def get_root():
    return {"Message": "Welcome to project akira"}


@app.get("/health")
def check_health():
    return {"Message": "Server running"}


app.include_router(query.router, prefix="/api/v1")
