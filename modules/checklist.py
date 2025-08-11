checklists = {
    "Company Incorporation": [
        "Articles of Association",
        "Memorandum of Association",
        "Board Resolution",
        "UBO Declaration Form",
        "Register of Members and Directors"
    ],
    "License Application": [
        "License Application Form",
        "Business Plan",
        "Financial Projections",
        "Compliance Manual",
        "Risk Management Framework",
        "Board Resolution for License Application"
    ],
    "Compliance Review": [
        "Annual Compliance Report",
        "Board Meeting Minutes",
        "Financial Statements",
        "Risk Assessment Report",
        "Compliance Monitoring Report"
    ]
}

def verify_checklist(process_type, uploaded_docs):
    required = checklists.get(process_type, [])
    missing = [doc for doc in required if doc not in uploaded_docs]
    return required, missing
