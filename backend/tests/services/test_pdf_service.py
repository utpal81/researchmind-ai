from pathlib import Path

from app.services.pdf_service import pdf_service


def test_read_pdf():

    pdf_path = Path("tests/data/resume.pdf")

    document = pdf_service.read(pdf_path)

    assert document.filename == "resume.pdf"

    assert len(document.pages) == document.page_count

    assert document.pages[0].page_number == 1

    assert len(document.pages[0].text) > 0