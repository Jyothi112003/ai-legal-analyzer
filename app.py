# app.py
import streamlit as st
from summarizer import extract_text_from_pdf, summarize_text
from vector_db import store_documents_in_vectordb, query_vectordb
from db_sqlite import init_db, store_document, get_all_documents

# Initialize the database
init_db()

st.set_page_config(page_title="Legal Document Summarizer & Chatbot", layout="wide")

st.title("📜 Legal Document Summarizer & Chatbot")

# File Uploader
uploaded_file = st.file_uploader("📂 Upload a legal PDF document", type=["pdf"])

if uploaded_file:
    pdf_path = "uploaded.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    # Extract and summarize text
    text = extract_text_from_pdf(pdf_path)
    if text and text != "No readable text found in the document.":
        summary = summarize_text(text)
        # Store in vector DB
        store_documents_in_vectordb(text, "uploaded_doc")
        # Store in SQLite
        store_document(uploaded_file.name, summary, text)

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
                st.warning("No relevant information found.")
    else:
        st.error("No readable text found in the document.")

# Section to view all stored documents
st.sidebar.title("Stored Documents")
docs = get_all_documents()
for doc in docs:
    doc_id, doc_name, doc_summary = doc
    if st.sidebar.button(f"View: {doc_name}", key=doc_id):
        st.write("### Stored Document Summary")
        st.write(doc_summary)
