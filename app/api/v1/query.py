from fastapi import APIRouter

router = APIRouter()


@router.post("/ask")
def ask():
    # ? Answer based on book
    pass
