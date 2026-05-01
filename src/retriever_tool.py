from langchain.tools import tool
from src.processing.vectorstore import retrievered

@tool
def retrieve_blog_posts(query: str) -> str:
    """Search and return information about Hill Climbing in The Kaggle Grandmaster Playbook."""
    retriever = retrievered()
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs])