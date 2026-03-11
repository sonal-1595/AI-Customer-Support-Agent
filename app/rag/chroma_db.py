from langchain_chroma import Chroma
from app.rag.embedding_model import embeddings_model


def load_chroma_db(collection_name, persist_directory):
    chroma_db = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings_model,
        persist_directory=persist_directory
    )
    return chroma_db


def create_chroma_db(collection_name, persist_directory, documents):
    chroma_db = Chroma.from_documents(
        documents=documents,
        embedding=embeddings_model,
        collection_name=collection_name,
        persist_directory=persist_directory
    )
    return chroma_db


def store_documents_in_chroma_db(chroma_db, documents):
    chroma_db.add_documents(documents)


def persist_chroma_db(chroma_db):
    pass