from pydantic import BaseModel


class UploadResponse(BaseModel):
    filename: str
    pages: int
    chunks: int


class HealthResponse(BaseModel):
    status: str
    version: str