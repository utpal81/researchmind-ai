from pathlib import Path

from app.services.pdf_service import pdf_service
from app.services.chunk_service import chunk_service


def test_chunking():

    document = pdf_service.read(
        Path("tests/data/resume.pdf")
    )

    chunks = chunk_service.chunk(document)

    assert len(chunks) == document.page_count

    assert chunks[0].page_number == 1

    assert chunks[0].document_filename == document.filename

    assert len(chunks[0].text.strip()) > 0