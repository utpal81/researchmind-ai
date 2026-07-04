from pathlib import Path

from app.services.pdf_service import pdf_service
from app.services.chunk_service import chunk_service
from app.services.embedding_service import embedding_service
from app.services.vector_store_service import vector_store_service


def test_add_embeddings():

    vector_store_service.clear()

    document = pdf_service.read(
        Path("tests/data/resume.pdf")
    )

    chunks = chunk_service.chunk(document)

    embedded_chunks = embedding_service.embed(chunks)

    vector_store_service.add(embedded_chunks)

    assert (
        vector_store_service.collection.count()
        == len(embedded_chunks)
    )