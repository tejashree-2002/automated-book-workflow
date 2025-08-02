
# === storage/chromadb_interface.py ===

import chromadb
from chromadb.utils import embedding_functions
import os

chroma_client = chromadb.Client()
embedding_fn = embedding_functions.DefaultEmbeddingFunction()
collection = chroma_client.get_or_create_collection("chapter_versions", embedding_function=embedding_fn)

def store_version(doc_id, text, metadata=None):
    print("\n>> Storing version in ChromaDB...")
    collection.add(
        documents=[text],
        ids=[doc_id],
        metadatas=[metadata or {}]
    )

def search_versions(query_text):
    print("\n>> Searching versions in ChromaDB...")
    results = collection.query(query_texts=[query_text], n_results=3)
    return results