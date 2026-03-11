from fastapi import APIRouter
from app.schemas.chat import HealthResponse
from app.core.config import settings

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to PawaIt AI API", "status": "online"}

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return {
        "status": "healthy",
        "ai_configured": settings.GEMINI_API_KEY is not None,
        "version": settings.VERSION
    }
