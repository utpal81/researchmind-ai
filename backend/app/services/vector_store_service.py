import chromadb
from app.schemas.embedding import EmbeddedChunk

from app.core.config import (
    VECTOR_DB_PATH,
    COLLECTION_NAME,
)


class VectorStoreService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=VECTOR_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            COLLECTION_NAME
        )

    def add(self, embedded_chunks: list[EmbeddedChunk]):

        for embedded_chunk in embedded_chunks:

            self.collection.add(
                ids=[str(embedded_chunk.chunk.chunk_id)],
                documents=[embedded_chunk.chunk.text],
                embeddings=[embedded_chunk.embedding],
                metadatas=[
                    {
                        "document": embedded_chunk.chunk.document_filename,
                        "page": embedded_chunk.chunk.page_number,
                        "chunk": embedded_chunk.chunk.chunk_number,
                    }
                ],
            )

    def clear(self):

        self.client.delete_collection(COLLECTION_NAME)

        self.collection = self.client.get_or_create_collection(
            COLLECTION_NAME
        )


    # serach for top k realated embedding chunks for the query
    def search( self, query_embedding: list[float], top_k: int = 5 ):

        results = self.collection.query( query_embeddings=[query_embedding],  n_results=top_k)

        return results


vector_store_service = VectorStoreService()