from pathlib import Path

from app.services.pdf_service import pdf_service
from app.services.chunk_service import chunk_service
from app.services.embedding_service import embedding_service


def test_embedding_generation():

    document = pdf_service.read(
        Path("tests/data/resume.pdf")
    )

    chunks = chunk_service.chunk(document)

    embedded_chunks = embedding_service.embed(chunks)

    assert len(embedded_chunks) == len(chunks)

    assert len(embedded_chunks[0].embedding) == 768