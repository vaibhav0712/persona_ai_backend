from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()
PINECONE_API = os.getenv("pinecone_api")


pc = Pinecone(api_key=PINECONE_API)
index_name = "book-rag"

print("Creating index:", index_name)
if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model": "llama-text-embed-v2",
            "field_map": {"text": "chunk_text"},
        },
    )
    print("Index created:", index_name)
else:
    print("Index exists:", index_name)
