from sentence_transformers import SentenceTransformer
from app.core.config import EMBEDDING_MODEL
from app.schemas.chunk import Chunk
from app.schemas.embedding import EmbeddedChunk

class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    def embed(
        self,
        chunks: list[Chunk]
    ) -> list[EmbeddedChunk]:

        embedded_chunks = []

        for chunk in chunks:

            vector = self.model.encode(chunk.text)

            embedded_chunks.append(

                EmbeddedChunk(
                    chunk=chunk,
                    embedding=vector.tolist()
                )

            )    

        return embedded_chunks
    
embedding_service = EmbeddingService()