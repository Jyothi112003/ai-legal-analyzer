import chromadb

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./vector_db")

# Create a collection
collection = chroma_client.get_or_create_collection(name="legal_docs")

def store_embedding(text, metadata):
    collection.add(
        documents=[text], 
        metadatas=[metadata], 
        ids=[metadata["id"]]
    )

def search_similar(query_text):
    results = collection.query(query_text, n_results=3)
    return results
