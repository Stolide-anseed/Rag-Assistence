from src.processing.loader import loader_docs
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import(
    CHUNK_SIZE,
    CHUNK_OVERLAP,

    )
def chunked(docs = loader_docs()):
    docs_list = [item for sublist in docs for item in sublist]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return text_splitter.split_documents(docs_list)