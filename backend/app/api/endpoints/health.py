from fastapi import APIRouter
from app.services.health_service import health_service

router = APIRouter()


@router.get("/health", tags=["Health"])
def health():
    return health_service.get_health()