# This project is a chat bot where you can have HR interviews with me 24/7
import streamlit as st
from helpers import generate_response
from content import content

# Massages list
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "system","content": content})

# Design of screen
st.header("HR Conversation Bot")
st.markdown("I don't have a huge budget for this project, I was only able to pay Openai $10. I ask you to consider this before you start chating with me. 😀")
st.divider()

# Loop of massages
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Generate a massage
if prompt := st.chat_input("Your massage"):
    st.chat_message("user").markdown(prompt)
    response = generate_response(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
