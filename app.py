import streamlit as st
from summarizer import extract_text_from_pdf, summarize_text
from vector_db import store_documents_in_vectordb, query_vectordb

# Streamlit Page Configuration
st.set_page_config(page_title="📜 Legal Document Summarizer & Chatbot", layout="wide")

st.title("📜 Legal Document Summarizer & Chatbot")

# 📂 File Uploader
uploaded_file = st.file_uploader("📂 Upload a legal PDF document", type=["pdf"])

if uploaded_file:
    # Save the uploaded file to a proper path
    pdf_path = "uploaded.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    # Extract text from the uploaded PDF
    text = extract_text_from_pdf(pdf_path)
    
    if text and text != "No readable text found in the document.":
        # Summarize text using Gemini API
        summary = summarize_text(text)

        # Store the document in VectorDB
        store_documents_in_vectordb(text, "uploaded_doc")

        # Display Summary
        st.subheader("📌 Summary")
        st.write(summary)

        # Chatbot Interface
        st.subheader("💬 Ask a question about the document")
        user_query = st.text_input("Enter your question here:")

        if user_query:
            results = query_vectordb(user_query)
            if results:
                st.write("**Answer:**", results[0].page_content)
            else:
                st.warning("No relevant information found in the document.")
    else:
        st.error("No readable text found in the document.")
