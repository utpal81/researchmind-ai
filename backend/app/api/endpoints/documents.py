from fastapi import APIRouter, File, UploadFile, HTTPException
from app.exceptions.document_exceptions import InvalidDocumentTypeError
from app.services.document_service import document_service
from app.schemas.document import Document

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload", response_model=Document)
def upload_document(file: UploadFile = File(...)):
    try:
        return document_service.create_document(file)
    except InvalidDocumentTypeError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
    )