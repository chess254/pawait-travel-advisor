from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000, description="The travel-related question from the user")

class QueryResponse(BaseModel):
    response: str
    status: str = "success"
    model_used: str = "gemini-pro-latest"

class HealthResponse(BaseModel):
    status: str
    ai_configured: bool
    version: str
