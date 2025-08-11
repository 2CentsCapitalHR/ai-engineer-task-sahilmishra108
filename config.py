from dotenv import load_dotenv  
import os

load_dotenv()

VECTOR_DB_PATH = "data/vector_store"
ADGM_DOCS_PATH = "data/reference_docs"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
GEMINI_MODEL = "gemini-pro"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")