import streamlit as st
import runpy

st.set_page_config(page_title="Gemini Multi-Tool", page_icon="⚪")

st.title("Gemini Multi-Tool")
choice = st.selectbox("Choose a feature:", ["Menu", "Text Q&A", "Image + Prompt"])

if choice == "Text Q&A":
    runpy.run_path("qna.py")

elif choice == "Image + Prompt":
    runpy.run_path("vision.py")
