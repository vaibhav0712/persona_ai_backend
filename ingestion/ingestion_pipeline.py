# I will html/text file in books folder in following format books/person/book1
# I will read each file at a time -> preprocess it if needed
# Perform the chunking -> store the result in what format? {First go with Simple Length based text splitter}
# Another idea is that do the chunking based on paragraphs to preserve the idea? <- this make more sense
# Make embeddings using pinecone

from dotenv import load_dotenv
from pinecone import Pinecone
from pathlib import Path
import time
import os

from ingestion_helper import format_chunks_for_pinecone, batch_iterable
from chunking import split_html

load_dotenv()

PINECONE_API = os.getenv("pinecone_api")
PINECONE_HOST = os.getenv("pinecone_host")
PINECONE_INDEX = os.getenv("pinecone_index")


pc = Pinecone(PINECONE_API)
pc_index = pc.Index(index=PINECONE_INDEX, host=PINECONE_HOST)


def upsert_book_in_pinecone(book_path):
    with open(book_path) as fp:

        content = fp.read()

        print("Chuking...")
        chunks = split_html(content)

        pinecone_chunks = format_chunks_for_pinecone(raw_chunks=chunks)
        print("Total records:", len(pinecone_chunks))

        print("Upserting in batches...")
        for batch in batch_iterable(pinecone_chunks):
            print("processing batch of ", len(batch))
            pc_index.upsert_records("Plato", batch)
            time.sleep(2)


if __name__ == "__main__":

    for book_id in ["1643"]:
        print("-" * 25)
        print("processing book:", book_id)
        book_path = Path.cwd() / "books" / f"pg{book_id}-images.html"

        upsert_book_in_pinecone(book_path=book_path)
        print("processed book:", book_id)
