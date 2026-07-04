from app.services.embedding_service import embedding_service
from app.services.vector_store_service import vector_store_service
from app.schemas.retrieval import RetrievedChunk


class RetrieverService:

    def retrieve(self, question: str, top_k: int = 5):

        query_embedding = embedding_service.embed_query( question)

        results = vector_store_service.search(query_embedding=query_embedding, top_k=top_k)

        retrieved_chunks=[]

        retrieved_chunks = []

        for chunk_id, text, metadata, distance in zip(
            results["ids"][0],
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):

            retrieved_chunks.append(
                RetrievedChunk(
                    chunk_id=chunk_id,
                    document_filename=metadata["document"],
                    page_number=metadata["page"],
                    chunk_number=metadata["chunk"],
                    text=text,
                    distance=distance,
                )
            )

        return retrieved_chunks    
    
retriever_service = RetrieverService()

        