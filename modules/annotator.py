import docx

def add_comment(doc_file, comments):
    try:
        doc = docx.Document(doc_file)
        for para in doc.paragraphs:
            for comment in comments:
                if comment.get("section_text") and comment["section_text"] in para.text:
                    para.text += f" [COMMENT: {comment['issue']} | Suggestion: {comment['suggestion']}]"
        reviewed_path = doc_file.name.replace(".docx", "_reviewed.docx")
        doc.save(reviewed_path)
        return reviewed_path
    except Exception as e:
        return f"Error adding comments: {str(e)}"
