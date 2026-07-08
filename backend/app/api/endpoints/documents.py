from fastapi import APIRouter, File, UploadFile, HTTPException
from app.exceptions.document_exceptions import InvalidDocumentTypeError
from app.services.document_service import document_service
from app.schemas.document import Document
from app.services.research_assistant_service import research_assistant_service
from app.services.vector_store_service import vector_store_service

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

# upload document endpoint 
@router.post("/upload", response_model=Document)
def upload_document(file: UploadFile = File(...)):
    try:
        return research_assistant_service.ingest_document(file)
    except InvalidDocumentTypeError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
    )

# delete vector db document endpoint 
@router.delete("/clear")
def clear_documents():

    vector_store_service.clear()

    return {"message": "Vector database cleared."}

