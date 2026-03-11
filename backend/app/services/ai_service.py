import logging
from google import genai
from google.genai import types
from app.core.config import settings

logger = logging.getLogger("pawait-api.ai_service")

class TravelAdvisor:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
        self.model_name = 'gemini-2.5-flash'
        self.system_instruction = (
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
        logger.info("Gemini AI configured successfully.")

    async def get_response(self, query: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=query,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instruction,
                )
            )
            return response.text or "I'm sorry, I couldn't generate a response for that."
        except Exception as e:
            logger.error(f"Error communicating with AI: {str(e)}")
            return f"Error communicating with AI: {str(e)}"

advisor = None
if settings.GEMINI_API_KEY:
    advisor = TravelAdvisor(settings.GEMINI_API_KEY)
else:
    logger.warning("GEMINI_API_KEY not found in environment. AI features will be disabled.")
