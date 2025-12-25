from fastapi import APIRouter

router = APIRouter()


@router.post("/book/ingest")
def ingest_book():
    # 1. download_book in local storage [DONE]
    # 2. Preprocess it and convert into .json
    # 3. Create embeddings of .json file
    # 4. Store embeddings in dbs
    # 5. Delete book from local storage
    pass
