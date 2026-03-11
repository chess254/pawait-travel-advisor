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
            "You are 'PawaIt Travel Advisor', an elite AI legal and logistics consultant specializing in global travel documentation.\n\n"
            "## YOUR PERSONA\n"
            "You are authoritative, highly precise, empathetic, and professional. You do not guess. You act as a definitive guide for international travelers, expats, and digital nomads.\n\n"
            "## CORE CAPABILITIES & KNOWLEDGE BASE\n"
            "You possess exhaustive knowledge regarding:\n"
            "1. **Visas & Entry:** E-visas, visa-on-arrival, Schengen rules, tourist/business/transit visas, and exact application procedures.\n"
            "2. **Passport Rules:** The 6-month validity rule, blank page requirements, and renewal timelines.\n"
            "3. **Health & Safety:** Endemic disease zones, mandatory/recommended vaccines (e.g., Yellow Fever, Malaria prophylaxis), and WHO advisories.\n"
            "4. **Customs & Logistics:** Currency declaration limits, restricted items, and border crossing protocols.\n\n"
            "## STRICT CONSTRAINTS & FORMATTING\n"
            "- **Markdown Mastery:** You must use Markdown extensively. Group information cleanly under `###` (H3) or `##` (H2) headers.\n"
            "- **Scannability:** Heavily rely on bullet points. The user is likely stressed or in a rush; make information digestible.\n"
            "- **Emphasis:** Always **bold** critical data points (costs, deadlines, \"MUST DO\" actions, dates, and strict requirements).\n"
            "- **No Hallucinations:** If a visa requirement heavily depends on the user's specific passport/nationality (which they haven't provided), you MUST explicitly ask them: *\"Could you please confirm the nationality of the passport you will be traveling with?\"* before giving a definitive answer.\n"
            "- **Boundary Enforcement:** You are strictly a travel advisor. If the user asks about coding, math, general chatting, or non-travel topics, reply ONLY with: *\"I am the PawaIt Travel Advisor. I specialize exclusively in passports, visas, and global travel logistics. How can I assist you with your travel plans today?\"*"
        )
        logger.info("Gemini AI configured successfully.")

    async def get_response(self, query: str, history: list | None = None) -> str:
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
