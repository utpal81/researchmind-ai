from pydantic import BaseModel
from datetime import datetime


class UploadResponse(BaseModel):
    filename: str
    page_count: int
    uploaded_at: datetime
    status: str