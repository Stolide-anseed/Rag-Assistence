from pydantic import BaseModel, Field
from typing import Literal
from langgraph.graph import MessagesState
from src.Prompts import GRADE_PROMPT
from src.generation.models import grade_model
class GradeDocuments(BaseModel):
    """Grade documents using a binary score for relevance check."""

    binary_score: Literal["yes", "no"] = Field(
        description="Relevance score: 'yes' if relevant, or 'no' if not relevant."
    )

grader_model = grade_model()

def grade_documents(state: MessagesState) -> Literal["generate_answer", "rewrite_question"]:
    """Determine whether the retrieved documents are relevant to the question."""
    question = state["messages"][0].content
    context = state["messages"][-1].content

    prompt = GRADE_PROMPT.format(question=question, context=context)

    response = (
        grader_model
        .with_structured_output(GradeDocuments)
        .invoke([{"role": "user", "content": prompt}])
    )

    if response.binary_score == "yes":
        return "generate_answer"
    else:
        return "rewrite_question"