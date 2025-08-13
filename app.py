import streamlit as st
import spacy

# Ensure model is available at runtime
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

st.title("Resume ↔ JD Matcher (Free)")
st.write("This is the updated version with runtime model loading to avoid build issues.")
