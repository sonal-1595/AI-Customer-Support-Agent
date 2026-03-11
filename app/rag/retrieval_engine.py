from app.rag.chroma_db import load_chroma_db

# load the persisted vector database
vector_db = load_chroma_db(
    collection_name="faq_collection",
    persist_directory="chroma_storage"
)


def retrieve_relevant_documents(query, top_k=5):
    relevant_docs = vector_db.similarity_search(query, k=top_k)
    return relevant_docs


def retrieve_and_format_response(query, top_k=5):
    relevant_docs = retrieve_relevant_documents(query, top_k)

    formatted_response = "\n\n".join(
        [doc.page_content for doc in relevant_docs]
    )

    return formatted_response

if __name__ == "__main__":
    query = input("Enter your query: ")

    response = retrieve_and_format_response(query)

    print("\nRetrieved Documents:\n")
    print(response)