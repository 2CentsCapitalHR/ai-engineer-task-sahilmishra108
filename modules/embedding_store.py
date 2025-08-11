import os
from sentence_transformers import SentenceTransformer
import chromadb
from config import ADGM_DOCS_PATH, VECTOR_DB_PATH, EMBEDDING_MODEL

def chunk_text(text, max_words=400):
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i+max_words])

def build_vector_store():
    # Ensure directories exist
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    os.makedirs(ADGM_DOCS_PATH, exist_ok=True)
    
    model = SentenceTransformer(EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
    collection = client.get_or_create_collection(name="adgm_docs")

    if not os.path.exists(ADGM_DOCS_PATH):
        print(f"Warning: {ADGM_DOCS_PATH} directory does not exist")
        return

    for fname in os.listdir(ADGM_DOCS_PATH):
        if fname.endswith(".txt"):
            try:
                with open(os.path.join(ADGM_DOCS_PATH, fname), "r", encoding="utf-8") as f:
                    text = f.read()
                for idx, chunk in enumerate(chunk_text(text)):
                    emb = model.encode(chunk).tolist()
                    collection.add(
                        documents=[chunk],
                        ids=[f"{fname}_{idx}"],
                        embeddings=[emb]
                    )
            except Exception as e:
                print(f"Error processing {fname}: {str(e)}")
    print("Vector store built successfully")

if __name__ == "__main__":
    build_vector_store()
