from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.retrieval_engine import retrieve_relevant_documents

router = APIRouter()

class FAQRequest(BaseModel):
    query: str


@router.post("/faq")
def get_faq(request: FAQRequest):

    docs = retrieve_relevant_documents(request.query)

    response = "\n\n".join([doc.page_content for doc in docs])

    return {"faq": response}