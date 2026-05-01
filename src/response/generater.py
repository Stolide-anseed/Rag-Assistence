from langgraph.graph import MessagesState
from src.response.res_model import res_model
from src.retriever_tool import retrieve_blog_posts

retriever_tool = retrieve_blog_posts

response_model = res_model()
def generate_query_or_respond(state: MessagesState):
    """Call the model to generate a response based on the current state. Given
    the question, it will decide to retrieve using the retriever tool, or simply respond to the user.
    """
    response = (
        response_model.bind_tools([retriever_tool]).invoke(state["messages"])
    )
    return {"messages": [response]}