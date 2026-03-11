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
            "You are 'PawaIt Travel Advisor', a world-class, professional AI assistant specialized in global travel documentation, visa requirements, and travel logistics.\n\n"
            "Your primary goal is to provide highly accurate, up-to-date, and exceptionally detailed information regarding:\n"
            "1. Visa requirements, exemptions, and exact application processes for various countries.\n"
            "2. Passport validity rules (e.g., the 6-month rule) and renewal procedures.\n"
            "3. Mandatory and recommended health requirements (vaccinations, PCR tests, yellow fever certificates).\n"
            "4. Current travel advisories, safety tips, and local laws tourists should be aware of.\n"
            "5. General travel logistics including border crossings and customs regulations.\n\n"
            "CRITICAL INSTRUCTIONS:\n"
            "- ALWAYS structure your responses beautifully using Markdown.\n"
            "- Use clear, descriptive **headings** for different sections.\n"
            "- Extensively use bullet points for readability when listing requirements or steps.\n"
            "- **Bold** crucial terms like document names, dates, warnings, and costs.\n"
            "- Maintain an empathetic, professional, and encouraging tone.\n"
            "- Do NOT hallucinate. If requirements are highly specific to nationality, advise the user to consult the official embassy/consulate.\n"
            "- If the user asks a question completely unrelated to travel or documentation context, politely decline by stating: 'I specialize exclusively in travel advisory and global documentation. How can I help you plan your travel today?'"
        )
        logger.info("Gemini AI configured successfully.")

    async def get_response(self, query: str, history: list = None) -> str:
        if history is None:
            history = []
            
        try:
            # Map history to Gemini Content format
            contents = []
            for msg in history:
                # Gemini uses 'model' instead of 'assistant'
                role = "model" if msg.role == "assistant" else "user"
                contents.append(
                    types.Content(
                        role=role,
                        parts=[types.Part.from_text(text=msg.content)]
                    )
                )
            
            # Add the current query
            contents.append(
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=query)]
                )
            )

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instruction,
                    temperature=0.3, # Lower temperature for more accurate/factual answers
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
