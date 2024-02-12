import openai
from dotenv import load_dotenv
import os
import streamlit as st


load_dotenv()



openai.api_key = "4fdaeb2a8fda4d9a9c4d2f95a5f52b54"
openai.api_base_url = "https://acc-alejandria-core-openaimagesound-pro.openai.azure.com"
openai.api_version = "2023-07-01-preview"
openai.api_type = "azure"

EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_EMBEDDING_ENGINE = 'mondongodb'
DIMENSION = 1536
GPT_MODEL = 'gpt-3.5-turbo-16k'
GPT_CHAT_ENGINE = "gepeto"
GPT_MODEL = 'gpt-4'
GPT_CHAT_ENGINE = "dictador"


st.title("chat")

if "messages" not in st.session_state:
  st.session_state["messages"] = [{"role": "assistant", "content": "Hola, soy ChatGPT, ¿En qué puedo ayudarte?"}]

for msg in st.session_state["messages"]:
  st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input():
  st.session_state["messages"].append({"role": "user", "content": user_input})
  st.chat_message("user").write(user_input)

  response = openai.chat.completions.create(
        model=GPT_MODEL,
        messages=st.session_state["messages"],
        engine=GPT_CHAT_ENGINE
    )
  
  responseMessage = response.choices[0].message.content
  st.session_state["messages"].append({"role": "assistant", "content": responseMessage})
  st.chat_message("assistant").write(responseMessage)
