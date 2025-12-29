from fastapi import APIRouter

from models.query_model import QueryRequest, QueryResponse
from core.config import settings
from services.retriveal_service import retrieve_chunks, format_chunks
from services.qa_service import generate_answer

router = APIRouter()


@router.post("/ask")
def ask(query: QueryRequest):
    user_question = query.question
    character = query.author or settings.default_character

    retrived_chunks = retrieve_chunks(
        namespace=character, question=user_question, top_k=3
    )
    context = format_chunks(chunks=retrived_chunks)

    generated_answer = generate_answer(
        question=user_question, character=character, context=context
    )

    response = {"question": user_question, "generated_answer": generated_answer}
    return QueryResponse(**response)
