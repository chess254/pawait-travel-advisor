from fastapi import APIRouter, HTTPException
from app.schemas.chat import QueryRequest, QueryResponse
from app.services.ai_service import advisor

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    if not advisor:
        raise HTTPException(status_code=500, detail="Gemini API Key is not configured on the server")

    try:
        response_text = await advisor.get_response(request.query, request.history)
        return QueryResponse(response=response_text)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Integration Error: {str(e)}")
