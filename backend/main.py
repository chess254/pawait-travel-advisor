import os
import time
import logging
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import google.generativeai as genai
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("pawait-api")

load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    logger.warning("GEMINI_API_KEY not found in environment. AI features will be disabled.")
else:
    genai.configure(api_key=api_key)
    logger.info("Gemini AI configured successfully.")

app = FastAPI(
    title="PawaIt AI Travel Assistant API",
    description="Professional backend for AI-powered travel documentation advisory.",
    version="1.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for the assessment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware for request timing
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Path: {request.url.path} | Method: {request.method} | Duration: {process_time:.4f}s")
    return response

# Custom Exception Handler
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "message": exc.detail, "path": request.url.path},
    )

# Models
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

@app.get("/")
async def root():
    return {"message": "Welcome to PawaIt AI API", "status": "online"}

@app.get("/health", response_model=HealthResponse)
async def health_check():
    return {
        "status": "healthy",
        "ai_configured": api_key is not None,
        "version": "1.1.0"
    }

class TravelAdvisor:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            system_instruction=(
                "You are 'PawaIt Travel Advisor', a professional assistant specialized in travel documentation. "
                "Your goal is to provide accurate information about: "
                "1. Visa requirements for various countries. "
                "2. Passport validity and application processes. "
                "3. Health requirements (vaccinations, PCR tests). "
                "4. Travel advisories and safety tips. "
                "5. General travel logistics. "
                "\n\nFormatting Rules: "
                "- Use clear headings. "
                "- Use bullet points for lists. "
                "- Bold important terms. "
                "- If asked something outside of travel, say: 'I specialize in travel advisory. How can I help you with your next trip?'"
            )
        )

    async def get_response(self, query: str) -> str:
        try:
            response = self.model.generate_content(query)
            return response.text
        except Exception as e:
            return f"Error communicating with AI: {str(e)}"

advisor = None
if api_key:
    advisor = TravelAdvisor(api_key)

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    if not advisor:
        raise HTTPException(status_code=500, detail="Gemini API Key is not configured on the server")

    try:
        response_text = await advisor.get_response(request.query)
        return QueryResponse(response=response_text)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Integration Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
