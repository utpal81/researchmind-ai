from uuid import UUID

from pydantic import BaseModel


class RetrievedChunk(BaseModel):

    chunk_id: UUID

    document_filename: str

    page_number: int

    chunk_number: int

    text: str

    distance: float