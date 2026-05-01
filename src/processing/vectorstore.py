from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from src.processing.chunking import chunked
from dotenv import load_dotenv
load_dotenv()
from config import(
    EMBIDDING,
    BASE_URL
)


def retrievered():
    doc_splits = chunked()
    vectorstore = InMemoryVectorStore.from_documents(
        documents=doc_splits,
        embedding=OpenAIEmbeddings(
        base_url = BASE_URL,
        model = EMBIDDING
        )
    )
    return vectorstore.as_retriever()
