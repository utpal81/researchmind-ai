class HealthService:
    """Service responsible for health-related operations."""

    @staticmethod
    def get_health():
        return {
            "status": "healthy",
            "service": "ResearchMind AI",
            "version": "0.1.0"
        }


health_service = HealthService()