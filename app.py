import streamlit as st
import json
from modules.doc_parser import extract_text, extract_clauses, detect_doc_type
from modules.checklist import verify_checklist
from modules.reviewer import review_text
from modules.rag_retriever import retrieve_context
from modules.annotator import add_comment
from modules.report_generator import generate_report

st.set_page_config(page_title="Corporate Agent", layout="wide")

st.title("Corporate Agent - ADGM Compliance Reviewer")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    process_type = st.selectbox(
        "Select Process Type",
        ["Company Incorporation", "License Application", "Compliance Review"],
        index=0
    )
    
    st.header("Instructions")
    st.markdown("""
    1. Upload your .docx legal documents
    2. Click 'Run Analysis' to start compliance review
    3. Review the generated compliance report
    4. Download annotated documents if needed
    """)

# Main content
uploaded_files = st.file_uploader(
    "Upload .docx legal documents", 
    type="docx", 
    accept_multiple_files=True,
    help="Upload multiple .docx files for compliance review"
)

if st.button("Run Clause-by-clause Analysis", type="primary") and uploaded_files:
    with st.spinner("Analyzing documents..."):
        uploaded_doc_types = []
        all_issues = []
        progress_bar = st.progress(0)
        
        for i, file in enumerate(uploaded_files):
            st.write(f"Processing {file.name}...")
            
            try:
                full_text = extract_text(file)
                if full_text.startswith("Error"):
                    st.error(f"Failed to extract text from {file.name}: {full_text}")
                    continue
                    
                doc_type = detect_doc_type(full_text)
                uploaded_doc_types.append(doc_type)

                clauses = extract_clauses(file)
                if clauses and clauses[0].startswith("Error"):
                    st.error(f"Failed to extract clauses from {file.name}: {clauses[0]}")
                    continue
                
                for idx, clause in enumerate(clauses):
                    if clause.strip():
                        context = retrieve_context(clause)
                        review_json = review_text(clause, context)
                        all_issues.append({
                            "document": doc_type,
                            "section": f"Clause {idx + 1}",
                            "review": review_json
                        })
                
                progress_bar.progress((i + 1) / len(uploaded_files))
                
            except Exception as e:
                st.error(f"Error processing {file.name}: {str(e)}")
                continue

        required_docs, missing_docs = verify_checklist(process_type, uploaded_doc_types) 
        report = generate_report(
            process_type, 
            uploaded_doc_types, 
            required_docs, 
            missing_docs, 
            all_issues
        )

    # Display results
    st.success("Analysis completed!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Document Summary")
        st.write(f"**Process Type:** {process_type}")
        st.write(f"**Documents Uploaded:** {len(uploaded_files)}")
        st.write(f"**Required Documents:** {len(required_docs)}")
        st.write(f"**Missing Documents:** {len(missing_docs)}")
        
        if missing_docs:
            st.warning("Missing required documents:")
            for doc in missing_docs:
                st.write(f"• {doc}")
    
    with col2:
        st.subheader("🔍 Issues Found")
        st.write(f"**Total Issues:** {len(all_issues)}")
        
        if all_issues:
            for issue in all_issues[:5]:  # Show first 5 issues
                st.write(f"**{issue['document']} - {issue['section']}**")
                if isinstance(issue['review'], str):
                    st.text(issue['review'][:200] + "..." if len(issue['review']) > 200 else issue['review'])
    
    # Download options
    st.subheader("📥 Download Results")
    
    # Download JSON report
    report_json = json.dumps(report, indent=2)
    st.download_button(
        label="Download Compliance Report (JSON)",
        data=report_json,
        file_name="compliance_report.json",
        mime="application/json"
    )
    
    # Show full report in expandable section
    with st.expander("View Full Compliance Report"):
        st.json(report)
