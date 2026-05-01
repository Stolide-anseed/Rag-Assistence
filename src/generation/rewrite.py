from langchain.messages import HumanMessage
from langgraph.graph import MessagesState

from src.response.generater import response_model
from src.Prompts import REWRITE_PROMPT



def rewrite_question(state: MessagesState):
    """Rewrite the original user question."""
    messages = state["messages"]
    question = messages[0].content
    prompt = REWRITE_PROMPT.format(question=question)
    response = response_model.invoke([{"role": "user", "content": prompt}])
    return {"messages": [HumanMessage(content=response.content)]}