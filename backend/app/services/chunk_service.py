from uuid import uuid4

from app.schemas.chunk import Chunk
from app.schemas.document import Document


class ChunkService:
    """Service responsible for splitting documents into chunks."""

    def chunk(self, document: Document) -> list[Chunk]:

        chunks = []

        for page in document.pages:

            chunks.append(
                Chunk(
                    chunk_id=uuid4(),
                    document_filename=document.filename,
                    page_number=page.page_number,
                    chunk_number=1,
                    text=page.text,
                )
            )

        return chunks


chunk_service = ChunkService()