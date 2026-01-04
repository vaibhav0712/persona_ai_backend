from fastapi import APIRouter, HTTPException

from models.query_model import QueryRequest, QueryResponse
from core.config import settings
from services.retriveal_service import retrieve_chunks, format_chunks
from services.qa_service import generate_answer

router = APIRouter()


@router.post("/ask")
async def ask(query: QueryRequest):
    user_question = query.question
    character = query.author or settings.default_character

    # PHASE 1 : Retrieval
    try:
        retrived_chunks = await retrieve_chunks(
            namespace=character, question=user_question, top_k=3
        )
        if not retrived_chunks:
            raise HTTPException(
                status_code=404, detail="No relevant context found in Knowledge Base."
            )
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Vector DB Error: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail="Knowledge Base service is currently unavailable.Please try again.",
        )

    context = format_chunks(chunks=retrived_chunks)

    # PHASE 2 : Generation
    try:
        generated_answer = await generate_answer(
            question=user_question, character=character, context=context
        )
    except Exception as e:
        print(f"LLM Error: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail="AI Generation service failed. The context was retrieved",
        )

    # Return
    response = {"question": user_question, "generated_answer": generated_answer}
    return QueryResponse(**response)
