from config import (
    MODEL,
    BASE_URL
)
from langchain.chat_models import init_chat_model

def res_model():
    response_model = init_chat_model(model = MODEL,
                                 temperature=0,
                                 base_url=BASE_URL)
    return response_model
