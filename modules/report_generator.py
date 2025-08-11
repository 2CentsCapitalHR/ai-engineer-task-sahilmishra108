import json

def generate_report(process, uploaded_docs, required_docs, missing_docs, issues):
    try:
        report = {
            "process": process,
            "documents_uploaded": len(uploaded_docs),
            "required_documents": len(required_docs),
            "missing_documents": missing_docs,
            "issues_found": issues
        }
        with open("review_report.json", "w") as f:
            json.dump(report, f, indent=2)
        return report
    except Exception as e:
        return {"error": f"Failed to generate report: {str(e)}"}