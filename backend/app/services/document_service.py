from pathlib import Path
import shutil
from app.exceptions.document_exceptions import InvalidDocumentTypeError
from app.services.pdf_service import pdf_service


UPLOAD_DIR = Path("storage/uploads")


class DocumentService:

    @staticmethod
    def ingest_document(file):

        ALLOWED_EXTENSIONS = {".pdf"}

        suffix = Path(file.filename).suffix.lower()

        if suffix not in ALLOWED_EXTENSIONS:
            raise InvalidDocumentTypeError( "Only PDF files are allowed." )

        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

        file_path = UPLOAD_DIR / file.filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        
        document=pdf_service.read(file_path)
        
        return document


document_service = DocumentService()