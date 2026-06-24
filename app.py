
import streamlit as st
import requests

st.set_page_config(page_title="Customer Support Agent")

st.title("Customer Support Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": user_input}
    )

    bot_reply = response.json()["response"]

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    st.rerun()
