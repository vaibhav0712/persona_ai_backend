from fastapi import APIRouter

from models.query_model import QueryRequest, QueryResponse
from core.config import settings


router = APIRouter()


@router.post("/ask")
def ask(query: QueryRequest):
    print(query.question)
    response = {"answer": query.question.lower()}
    return QueryResponse(**response)
