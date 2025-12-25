from fastapi import FastAPI
from api.v1 import book
from api.v1 import query


app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "Welcome to project akira"}


app.include_router(book.router, prefix="/api/v1")
app.include_router(query.router, prefix="/api/v1")
