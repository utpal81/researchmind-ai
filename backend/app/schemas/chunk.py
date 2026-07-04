from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Chunk(BaseModel):
    chunk_id: UUID
    document_filename: str
    page_number: int
    chunk_number: int
    section: Optional[str]=None
    text: str
    