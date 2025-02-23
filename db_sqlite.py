import sqlite3
import os

DB_PATH = "legal_summaries.db"

def init_db():
    """Initialize the SQLite database with a table for documents."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Create a table for storing PDF name, summary, and extracted text
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_name TEXT NOT NULL,
            summary TEXT,
            full_text TEXT
        )
    """)
    conn.commit()
    conn.close()

def store_document(doc_name, summary, full_text):
    """Store a document's summary and full text into SQLite."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO documents (doc_name, summary, full_text)
        VALUES (?, ?, ?)
    """, (doc_name, summary, full_text))
    conn.commit()
    conn.close()

def get_all_documents():
    """Retrieve all documents from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, doc_name, summary FROM documents")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_document_by_id(doc_id):
    """Retrieve a single document by its ID."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT doc_name, summary, full_text FROM documents WHERE id=?", (doc_id,))
    row = cursor.fetchone()
    conn.close()
    return row
