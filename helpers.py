import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

my_keys = os.getenv("api_key")

client = OpenAI(api_key=my_keys)

def generate_response(prompt):
    st.session_state.messages.append({"role":"user","content": prompt})
    AI_response = client.chat.completions.create(
        model="gpt-4-1106-vision-preview",
        messages= st.session_state.messages,
        )
    return AI_response.choices[0].message.content