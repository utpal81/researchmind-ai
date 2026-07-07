from uuid import uuid4

from app.schemas.retrieval import RetrievedChunk
from app.services.prompt_builder_service import prompt_builder_service


def test_build_prompt():

    chunks = [
        RetrievedChunk(
            chunk_id=uuid4(),
            document_filename="sample.pdf",
            page_number=1,
            chunk_number=1,
            text="Adam optimizer was used.",
            distance=0.10,
        )
    ]

    prompt = prompt_builder_service.build_prompt(
        question="Which optimizer was used?",
        retrieved_chunks=chunks,
    )

    assert "Adam optimizer" in prompt
    assert "Which optimizer was used?" in prompt