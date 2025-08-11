import google.generativeai as genai
from config import GEMINI_MODEL, GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def review_text(clause, context):
    prompt = f"""
    You are an ADGM legal compliance reviewer. Review the single clause for compliance:

    clause: {clause}
    Relevant ADGM Law/Template Context: {context}

    Identify:
    1. Issue or red flag
    2. Relevant ADGM regulations/article
    3. Severity (High, Medium, Low)
    4. Suggested compliant rewrite

    Return JSON with keys: section_text, issue, severity, suggestion.
    """
    try:
        response = genai.GenerativeModel(
            model=GEMINI_MODEL
        ).generate_content(prompt)
        return response.text
    except Exception as e:
        return {"error": f"Failed to review text: {str(e)}"}
