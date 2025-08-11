<<<<<<< HEAD
# Corporate Agent - ADGM Compliance Reviewer

A Streamlit-based application for automated compliance review of legal documents for ADGM (Abu Dhabi Global Market) regulatory requirements.

## Features

- **Document Upload**: Upload multiple .docx legal documents
- **Clause-by-Clause Analysis**: Automatic extraction and analysis of document clauses
- **Compliance Checking**: AI-powered review against ADGM regulations
- **Checklist Verification**: Verify required documents for different processes
- **Report Generation**: Generate comprehensive compliance reports
- **Document Annotation**: Add comments and suggestions to documents

## Supported Process Types

1. **Company Incorporation**
   - Articles of Association
   - Memorandum of Association
   - Board Resolution
   - UBO Declaration Form
   - Register of Members and Directors

2. **License Application**
   - License Application Form
   - Business Plan
   - Financial Projections
   - Compliance Manual
   - Risk Management Framework
   - Board Resolution for License Application

3. **Compliance Review**
   - Annual Compliance Report
   - Board Meeting Minutes
   - Financial Statements
   - Risk Assessment Report
   - Compliance Monitoring Report

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd corporate-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

4. Set up the vector database:
```bash
python modules/embedding_store.py
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided URL

3. Upload your .docx legal documents

4. Select the process type from the sidebar

5. Click "Run Clause-by-clause Analysis"

6. Review the generated compliance report

7. Download the results as needed

## Project Structure

```
corporate-agent/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── data/
│   ├── reference_docs/  # ADGM reference documents
│   └── vector_store/    # Vector database for embeddings
└── modules/
    ├── __init__.py
    ├── annotator.py     # Document annotation functionality
    ├── checklist.py     # Document checklist verification
    ├── doc_parser.py    # Document parsing and text extraction
    ├── embedding_store.py # Vector database management
    ├── rag_retriever.py # RAG-based context retrieval
    ├── report_generator.py # Report generation
    └── reviewer.py      # AI-powered compliance review
```

## Dependencies

- **streamlit**: Web application framework
- **python-docx**: Microsoft Word document processing
- **langchain**: AI/ML framework
- **chromadb**: Vector database
- **sentence-transformers**: Text embeddings
- **google-generativeai**: Gemini AI integration
- **docxcompose**: Document composition
- **pandas**: Data manipulation
- **python-dotenv**: Environment variable management

## Configuration

The application can be configured through the `config.py` file:

- `VECTOR_DB_PATH`: Path to the vector database
- `ADGM_DOCS_PATH`: Path to reference documents
- `EMBEDDING_MODEL`: Sentence transformer model for embeddings
- `GEMINI_MODEL`: Gemini AI model for text generation
- `GEMINI_API_KEY`: API key for Gemini AI

## Error Handling

The application includes comprehensive error handling for:
- File upload issues
- Document parsing errors
- AI API failures
- Vector database connection issues
- Report generation problems

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please open an issue in the repository.
=======
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vgbm4cZ0)
>>>>>>> 73c6cd0c8cda3832a820bd3b44f6bc58a0db4ccd
