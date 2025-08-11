import chromadb
from sentence_transformers import SentenceTransformer
from config import VECTOR_DB_PATH, EMBEDDING_MODEL

# Create persistent client & collection only once
_client = None
_collection = None
_model = None

def _initialize_components():
    global _client, _collection, _model
    if _client is None:
        _client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
        try:
            _collection = _client.get_collection("adgm_docs")
        except:
            _collection = _client.create_collection("adgm_docs")
        _model = SentenceTransformer(EMBEDDING_MODEL)

def retrieve_context(query, top_k=3):
    """Retrieve top_k relevant context chunks for a given query."""
    _initialize_components()
    try:
        emb = _model.encode(query).tolist()
        results = _collection.query(query_embeddings=[emb], n_results=top_k)
        docs = results["documents"][0]
        return "\n\n".join(docs)
    except Exception as e:
        return f"Error retrieving context: {str(e)}"
