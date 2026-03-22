import chromadb
from chromadb.utils import embedding_functions

# Initialize ChromaDB client
client = chromadb.Client()

# Use default embedding function
embedding_fn = embedding_functions.DefaultEmbeddingFunction()

def save_to_memory(topic: str, content: str, doc_id: str) -> str:
    """Save research content to ChromaDB vector store."""
    try:
        collection = client.get_or_create_collection(
            name="research_memory",
            embedding_function=embedding_fn
        )
        
        collection.upsert(
            documents=[content],
            ids=[doc_id],
            metadatas=[{"topic": topic}]
        )
        return f"Saved to memory: {doc_id}"
    
    except Exception as e:
        return f"Memory save failed: {str(e)}"


def retrieve_from_memory(query: str, n_results: int = 3) -> str:
    """Retrieve relevant content from ChromaDB."""
    try:
        collection = client.get_or_create_collection(
            name="research_memory",
            embedding_function=embedding_fn
        )
        
        results = collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        if not results['documents'][0]:
            return "No relevant memory found."
        
        return "\n---\n".join(results['documents'][0])
    
    except Exception as e:
        return f"Memory retrieval failed: {str(e)}"