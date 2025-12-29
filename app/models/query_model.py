from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str
    author: str = "Plato"


class QueryResponse(BaseModel):
    question: str
    generated_answer: str
