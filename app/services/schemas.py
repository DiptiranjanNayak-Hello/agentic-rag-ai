from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    query: str
    session_id: str
    user_id: Optional[str] = "default_user"

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]
    intermediate_steps: List[str]