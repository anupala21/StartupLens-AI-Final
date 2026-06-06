import streamlit as st
import requests

st.set_page_config(
    page_title="StartupLens AI",
    layout="wide"
)

st.title("🚀 StartupLens AI")

idea = st.text_area(
    "Enter Your Startup Idea"
)

if st.button("Validate Idea"):

    response = requests.post(
        "http://127.0.0.1:8000/validate",
        json={"idea": idea}
    )

    result = response.json()

    st.success("Idea Submitted")

    st.write(result)