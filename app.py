import streamlit as st
from crewai import Agent, Crew, Process
from langchain_groq import ChatGroq

st.set_page_config(page_title="منصة الذكاء الاصطناعي والإبداع")
st.title("أدوات الذكاء الاصطناعي والإبداع")

st.write("Midjourney للصور، Canva للتصميم، Recraft للمتجهات، وKling للمونتاج.")

user_prompt = st.text_input("أدخل سؤالك أو الموضوع الذي تود تحليله:")

if st.button("بدء المعالجة"):
    if user_prompt:
        st.write("يتم الآن معالجة طلبك...")
