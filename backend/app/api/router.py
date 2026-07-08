from fastapi import APIRouter

from app.api.endpoints.health import router as health_router
from app.api.endpoints.documents import router as document_router
from app.api.endpoints import chat

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(document_router)
api_router.include_router(chat.router)