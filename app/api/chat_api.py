from fastapi import APIRouter
from pydantic import BaseModel
from app.agent.decision_agent import DecisionAgent

router = APIRouter()

agent = DecisionAgent()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = agent.generate_response(request.message)
    return ChatResponse(response=reply)