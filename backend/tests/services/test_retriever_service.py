from pathlib import Path

from app.services.pdf_service import pdf_service
from app.services.chunk_service import chunk_service
from app.services.embedding_service import embedding_service
from app.services.vector_store_service import vector_store_service
from app.services.retriever_service import retriever_service


def test_retrieve():

    vector_store_service.clear()

    document = pdf_service.read(
        Path("tests/data/sample.pdf")
    )

    chunks = chunk_service.chunk(document)

    embedded_chunks = embedding_service.embed(chunks)

    vector_store_service.add(embedded_chunks)

    retrieved = retriever_service.retrieve(
        "What is this document about?"
    )

    assert len(retrieved) > 0

    assert retrieved[0].document_filename == document.filename