import streamlit as st
from summarizer import extract_text_from_pdf, summarize_text

st.title("📜 Legal Document Summarizer ")

# File uploader
uploaded_file = st.file_uploader("📂 Upload a legal PDF document", type=["pdf"])

if uploaded_file is not None:
    temp_file_path = "temp_uploaded.pdf"

    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.read())  # Save uploaded file

    # Extract text
    text = extract_text_from_pdf(temp_file_path)

    if text.strip():
        with st.spinner("🔍 Summarizing... Please wait"):
            summary = summarize_text(text)
        
        st.subheader("📌 Summary")
        st.write(summary)
    else:
        st.error("⚠️ No readable text found in the document.")
