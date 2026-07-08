from fastapi import APIRouter
from app.schemas.answer import Answer
from app.schemas.api import QuestionRequest
from app.services.research_assistant_service import research_assistant_service

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/ask")
def ask(request: QuestionRequest, response_model=Answer):

    return research_assistant_service.ask(
        request.question
    )