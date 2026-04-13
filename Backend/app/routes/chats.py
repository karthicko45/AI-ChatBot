from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm import get_ai_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(request: ChatRequest):
    reply = get_ai_response(request.message)
    return {"reply": reply}