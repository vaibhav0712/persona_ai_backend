import re


def format_book_title(title):
    title = re.sub(r"[^a-zA-Z0-9]", "", title)
    return "".join(title.split(" ")).lower()


def format_chunks_for_pinecone(raw_chunks):
    new_chunks = []
    previous_book = "THE TRIAL Franz Kafka"
    previous_chapter = "INTRODUCTION"

    for inx, chunk in enumerate(raw_chunks):

        # Edge case where book_title and chapter is missing or not detected but <p> text is there
        if not "book" in chunk.metadata:
            chunk.metadata["book"] = previous_book
        if not "chapter" in chunk.metadata:
            chunk.metadata["chapter"] = previous_chapter

        if "book" in chunk.metadata and "chapter" in chunk.metadata:
            previous_chapter = chunk.metadata.get("chapter")  # For edge case
            previous_book = chunk.metadata.get("book")  # For edge case

            formated_book_title = format_book_title(chunk.metadata.get("book"))
            pinecone_formt = {
                "_id": f"{formated_book_title}#chunk{inx}",
                "chunk_text": chunk.page_content,
                "document_id": formated_book_title,
                "book": chunk.metadata.get("book"),
                "chapter": chunk.metadata.get("chapter"),
            }
            new_chunks.append(pinecone_formt)

    return new_chunks


def batch_iterable(iterable, batch_size=16):
    for i in range(0, len(iterable), batch_size):
        yield iterable[i : i + batch_size]
