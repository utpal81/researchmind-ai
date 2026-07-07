from pydantic import BaseModel

from app.schemas.retrieval import RetrievedChunk


class Answer(BaseModel):
    answer: str
    sources: list[RetrievedChunk]