from google import genai

from app.core.config import settings


class LLMService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def answer(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
        )

        return response.text


llm_service = LLMService()