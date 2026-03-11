from app.rag.chroma_db import create_chroma_db, persist_chroma_db
from app.rag.faq_loader import load_faqs_from_json

documents = load_faqs_from_json("data/faq_dataset.json")

chroma_db = create_chroma_db(
    collection_name="faq_collection",
    persist_directory="chroma_storage",
    documents=documents
)

persist_chroma_db(chroma_db)

print("FAQs successfully stored in Chroma DB")