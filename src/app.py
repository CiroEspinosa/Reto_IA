import openai
import streamlit as st
from pinecone import Pinecone, ServerlessSpec





PINECONE_API_KEY = st.secrets["PINECONE_API_KEY_V2"]
PINECONE_ENV = st.secrets["PINECONE_ENV"]
PINECONE_INDEX_NAME = st.secrets["PINECONE_INDEX_NAME"]

pc = Pinecone(api_key=PINECONE_API_KEY)

pinecone.init(api_key=PINECONE_API_KEY)
connector = pinecone.Index(index_name=PINECONE_INDEX_NAME)

api_key = st.secrets["OPENAI_API_KEY"]
api_base = st.secrets["OPENAI_API_BASE"]
api_version = st.secrets["OPENAI_API_VERSION"]
api_type = st.secrets["OPENAI_API_TYPE"]


openai.api_key = api_key
openai.api_base = api_base
openai.api_version = api_version
openai.api_type = api_type

EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_EMBEDDING_ENGINE = 'mondongodb'
DIMENSION = 1536
# GPT_MODEL = 'gpt-3.5-turbo-16k'
# GPT_CHAT_ENGINE = "gepeto"
GPT_MODEL = 'gpt-4'
GPT_CHAT_ENGINE = "dictador"


st.title("Chatbot")
is_pdf_chatbot = st.checkbox("PDF chatbot")
if "messages" not in st.session_state:
  st.session_state["messages"] = [{"role": "assistant", "content": "Hola, soy ChatGPT, ¿En qué puedo ayudarte?"}]

for msg in st.session_state["messages"]:
  st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input():
  st.session_state["messages"].append({"role": "user", "content": user_input})
  st.chat_message("user").write(user_input)

  if is_pdf_chatbot:
    """user_input_vector = my_vectorizer_function(user_input)
    pinecone_result = connector.query(queries=[user_input_vector], top_k=5)
    relevant_info_from_pdf = get_info_from_pinecone_result(pinecone_result)
    responseMessage = relevant_info_from_pdf"""
  else:
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=st.session_state["messages"],
        engine=GPT_CHAT_ENGINE,
        max_tokens=DIMENSION
    )
    responseMessage = response['choices'][0]['message']['content']

  st.session_state["messages"].append({"role": "assistant", "content": responseMessage})
  st.chat_message("assistant").write(responseMessage)

pinecone.deinit()  
