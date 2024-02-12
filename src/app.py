import openai
import streamlit as st

# Configuración de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]
openai.api_base_url = "https://acc-alejandria-core-openaimagesound-pro.openai.azure.com"
openai.api_version = "2023-07-01-preview"
openai.api_type = "azure"

# Parámetros del chatbot
GPT_MODEL = 'gpt-3.5-turbo-16k'
GPT_CHAT_ENGINE = "gepeto"

st.title("Chatbot")

# Verificar si existe la lista de mensajes en la sesión
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Mostrar todos los mensajes en la lista
for msg in st.session_state["messages"]:
    st.write(f"{msg['role']}: {msg['content']}")

# Esperar la entrada del usuario
user_input = st.text_input("Usted:", "")

# Si se proporciona una entrada de usuario, generar la respuesta del bot
if user_input:
    # Agregar el mensaje del usuario a la lista
    st.session_state["messages"].append({"role": "Usted", "content": user_input})

    # Generar la respuesta del bot con OpenAI
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=st.session_state["messages"],
        engine=GPT_CHAT_ENGINE
    )
  
    # Agregar la respuesta del bot a la lista
    responseMessage = response['choices'][0]['message']['content']
    st.session_state["messages"].append({"role": "Bot", "content": responseMessage})
