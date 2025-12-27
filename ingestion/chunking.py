from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    HTMLHeaderTextSplitter,
)


def split_html(html_string: str):
    headers_to_split_on = [
        ("h1", "book"),
        ("h2", "chapter"),
    ]
    header_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    html_head_splits = header_splitter.split_text(html_string)
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=5000, chunk_overlap=100
    )
    docs = recursive_splitter.split_documents(html_head_splits)
    return docs
