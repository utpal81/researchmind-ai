from pydantic import BaseModel

from app.schemas.chunk import Chunk


class EmbeddedChunk(BaseModel):
    chunk: Chunk
    embedding: list[float]