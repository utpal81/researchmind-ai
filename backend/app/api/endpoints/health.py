from fastapi import APIRouter
from app.services.health_service import health_service

router = APIRouter()


@router.get("/health", tags=["Health"], response_model=HealthResponse)
def health():
    return health_service.get_health()