from langchain.chat_models import init_chat_model
from config import (
    MODEL,
    BASE_URL
)

def grade_model():
    gra_model = init_chat_model(model=MODEL,
                                     temperature=0,
                                     base_url=BASE_URL)
    return gra_model
