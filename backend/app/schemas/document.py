from pydantic import BaseModel
from typing import Optional

class DocumentPage(BaseModel):
    page_number: int
    text: str


class DocumentMetadata(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    subject: Optional[str] = None


class Document(BaseModel):
    filename: str
    page_count: int
    metadata: DocumentMetadata
    pages: list[DocumentPage]


