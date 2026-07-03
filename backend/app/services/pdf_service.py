from pathlib import Path
import fitz
from app.schemas.document import (Document, DocumentMetadata, DocumentPage)


class PDFService:
    """Service responsible for reading PDF documents."""

    # open pdf and build the document
    def read(self, pdf_path: Path) -> Document:
        
        with fitz.open(pdf_path) as pdf:

            metadata = self._extract_metadata(pdf)

            pages = self._extract_pages(pdf)

            return Document(
                filename=pdf_path.name,
                metadata=metadata,
                page_count=len(pages),
                pages=pages,
            )

    # extract metadata
    def _extract_metadata(self, pdf) -> DocumentMetadata:

        metadata = pdf.metadata

        return DocumentMetadata(
            title=metadata.get("title"),
            author=metadata.get("author"),
            subject=metadata.get("subject"),
        )

    # extract pages
    def _extract_pages(self, pdf) -> list[DocumentPage]:

        pages = []

        for page_number, page in enumerate(pdf, start=1):

            pages.append(
                DocumentPage(
                    page_number=page_number,
                    text=page.get_text(),
                )
            )

        return pages
        


pdf_service = PDFService()