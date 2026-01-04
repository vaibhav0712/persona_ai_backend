from db.connection import get_pinecone_index


async def retrieve_chunks(
    namespace: str, question: str, top_k: int = 2
) -> list[dict[str:str]]:
    inx = get_pinecone_index()
    response = await inx.search_records(
        namespace=namespace,
        query={
            "inputs": {"text": question},
            "top_k": top_k,
        },
        fields=["book", "chapter", "chunk_text"],
    )
    return response.result.hits


def format_chunks(chunks: list[dict[str:str]]) -> str:
    context = []
    for chunk in chunks:
        merged = f"book:{chunk.fields['book']} -> chapter:{chunk.fields['chapter']} -> text:{chunk.fields['chunk_text']}"
        context.append(merged)

    return " \n\n".join(context)


# res = retrieve_chunks("Plato", "Life is happy")
# print(res)
# print(format_chunks(res))
