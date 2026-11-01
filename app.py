import streamlit as st
from crewai import Agent, Crew, Process
from langchain_groq import ChatGroq

st.set_page_config(page_title="تطبيق وكلاء الذكاء الاصطناعي")
st.title("وكلاء الذكاء الاصطناعي")
