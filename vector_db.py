import chromadb
from chromadb.utils import embedding_functions
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize ChromaDB Client
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Initialize Google's embedding function
embedding_function = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)

# Create or Load a Chroma Collection
collection = chroma_client.get_or_create_collection(name="legal_documents")

def store_documents_in_vectordb(text, doc_id):
    """
    Stores extracted document text into ChromaDB with Google Gemini embeddings.
    """
    chunks = text.split("\n\n")  # Split by paragraphs
    
    documents = []
    for i, chunk in enumerate(chunks):
        if chunk.strip():
            documents.append(Document(page_content=chunk, metadata={"doc_id": doc_id, "chunk_id": i}))

    # Store in ChromaDB
    vectorstore = Chroma(collection_name="legal_documents", embedding_function=embedding_function)
    vectorstore.add_documents(documents)
    print(f"✅ Stored {len(documents)} chunks in the vector database.")

def query_vectordb(query_text):
    """
    Queries ChromaDB to find the most relevant text chunk based on user input.
    """
    vectorstore = Chroma(collection_name="legal_documents", embedding_function=embedding_function)
    results = vectorstore.similarity_search(query_text, k=2)
    return results
