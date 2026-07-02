from fastapi import FastAPI

app = FastAPI(
    title="ResearchMind AI",
    description="AI-powered platform for scientific literature analysis",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ResearchMind AI"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }