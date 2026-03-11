from typing import List, Optional
from pydantic import BaseModel, Field

class ChatMessage(BaseModel):
    role: str = Field(..., description="The role of the message sender, either 'user' or 'assistant'")
    content: str = Field(..., description="The content of the message")

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000, description="The travel-related question from the user")
    history: Optional[List[ChatMessage]] = Field(default=[], description="Previous conversation context")

class QueryResponse(BaseModel):
    response: str
    status: str = "success"
    model_used: str = "gemini-pro-latest"

class HealthResponse(BaseModel):
    status: str
    ai_configured: bool
    version: str
