import re


def format_book_title(title):
    title = re.sub(r"[^a-zA-Z0-9]", "", title)
    return "".join(title.split(" ")).lower()


def format_chunks_for_pinecone(raw_chunks):
    new_chunks = []
    for inx, chunk in enumerate(raw_chunks):
        # CAN ADD LENGTH FILTER FOR PARAGRAPH
        if "book" in chunk.metadata and "chapter" in chunk.metadata:
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
