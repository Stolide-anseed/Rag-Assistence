from langchain_community.document_loaders import WebBaseLoader
from config import (
    URLS
)
def loader_docs():
    docs = [WebBaseLoader(url).load() for url in URLS]
    return docs


