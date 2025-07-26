import streamlit as st
from inference import generate_text

st.title("AI Text Generator ✨")
prompt = st.text_input("Enter your prompt here")

if st.button("Generate"):
    if prompt.strip() != "":
        result = generate_text(prompt)
        st.success(result)
    else:
        st.warning("Please enter a valid prompt.")
