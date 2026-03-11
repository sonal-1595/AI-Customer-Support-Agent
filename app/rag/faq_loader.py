import json
from langchain_core.documents import Document

def load_faqs_from_json(file_path):
    with open(file_path, 'r') as f:
        faqs = json.load(f)
    
    documents = []
    for faq in faqs:
        question = faq.get('question', '')
        answer = faq.get('answer', '')
        content = f"Q: {question}\nA: {answer}"
        
        doc = Document(
            page_content=content,
            metadata={
                'source': "faq_dataset.json",
                'question': question,   
            }
        )
        documents.append(doc)
    
    return documents

