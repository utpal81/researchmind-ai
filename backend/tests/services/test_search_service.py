from pathlib import Path

from app.services.pdf_service import pdf_service
from app.services.chunk_service import chunk_service
from app.services.embedding_service import embedding_service
from app.services.vector_store_service import vector_store_service


def test_semantic_search():

    vector_store_service.clear()

    document = pdf_service.read( Path("tests/data/resume.pdf") )

    chunks = chunk_service.chunk(document)

    embedded_chunks = embedding_service.embed(chunks)

    vector_store_service.add(embedded_chunks)

    query = "What is this document about?"

    query_embedding = embedding_service.embed_query(query)

    print("Collection count:", vector_store_service.collection.count())

    results = vector_store_service.search(query_embedding)

    print("\n")
    print(results)

    assert len(results["ids"][0]) > 0