from langchain.llms import openai
from langchain.chat_models import ChatOpenAI

def ask_ai(query):
    llm = openai.OpenAI()
    response = llm.predict(query)
    return(response)