import streamlit as st
from langchain_groq import ChatGroq
import os

# Initialize Groq client
llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

st.set_page_config(page_title="Artificial Intelligence tools and creativity")
st.title("Artificial intelligence and creativity tools")

st.write(
    "For vectors: Recraft, for design: Canva, for images: Midjourney, for editing: Kling and Veed."
)

user_prompt = st.text_input("Enter your question or the topic you want to analyze:")

if st.button("Start processing"):
    if user_prompt:
        st.write("Your request is being processed...")
        response = llm.invoke(user_prompt)
        st.write(response.content)
``` الكود في ملف app dot py على—
