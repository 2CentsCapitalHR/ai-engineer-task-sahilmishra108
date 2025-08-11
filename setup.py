#!/usr/bin/env python3
"""
Setup script for Corporate Agent - ADGM Compliance Reviewer
"""

import os
import sys
from pathlib import Path

def create_directories():
    """Create necessary directories if they don't exist."""
    directories = [
        "data/reference_docs",
        "data/vector_store"
    ]
    
    for directory in directories:
        try:
            Path(directory).mkdir(parents=True, exist_ok=True)
            print(f"✓ Directory ready: {directory}")
        except Exception as e:
            print(f"✓ Directory already exists: {directory}")

def create_env_file():
    """Create .env file if it doesn't exist."""
    env_file = Path(".env")
    if not env_file.exists():
        env_content = """# Gemini AI API Key
# Get your API key from: https://makersuite.google.com/app/apikey
GEMINI_API_KEY=your_gemini_api_key_here

# Optional: Override default configuration
# VECTOR_DB_PATH=data/vector_store
# ADGM_DOCS_PATH=data/reference_docs
# EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
# GEMINI_MODEL=gemini-pro
"""
        with open(env_file, "w") as f:
            f.write(env_content)
        print("✓ Created .env file")
        print("⚠️  Please update the GEMINI_API_KEY in .env file")
    else:
        print("✓ .env file already exists")

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import streamlit
        import docx
        import langchain
        import chromadb
        import sentence_transformers
        import google.generativeai
        import pandas
        import dotenv
        print("✓ All required dependencies are installed")
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False
    return True

def main():
    """Main setup function."""
    print("Setting up Corporate Agent - ADGM Compliance Reviewer")
    print("=" * 50)
    
    # Create directories
    create_directories()
    
    # Create .env file
    create_env_file()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("\nSetup completed successfully!")
    print("\nNext steps:")
    print("1. Update the GEMINI_API_KEY in .env file")
    print("2. Add reference documents to data/reference_docs/")
    print("3. Run: python modules/embedding_store.py")
    print("4. Run: streamlit run app.py")

if __name__ == "__main__":
    main()
