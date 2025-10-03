from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional

from .agent import NandaAgent
from .config import NANDA_SHARED_SECRET

app = FastAPI(title="NANDA Adapter Wrapped Agent")
agent = NandaAgent()


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[ChatMessage]


@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/chat")
async def chat(
    req: ChatRequest,
    x_nanda_secret: Optional[str] = Header(default=None),
) -> Dict[str, Any]:
    if NANDA_SHARED_SECRET and x_nanda_secret != NANDA_SHARED_SECRET:
        return JSONResponse(status_code=401, content={"error": "unauthorized"})

    messages: List[Dict[str, Any]] = [message.model_dump() for message in req.messages]
    answer = await agent.run(messages)
    return {"reply": answer}
