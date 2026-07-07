from sentence_transformers import SentenceTransformer
from app.core.config import settings
from app.schemas.chunk import Chunk
from app.schemas.embedding import EmbeddedChunk

class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer( settings.EMBEDDING_MODEL)

    # embedding for the chunks
    def embed( self, chunks: list[Chunk]) -> list[EmbeddedChunk]:

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
    
    
    # embedding for the query
    def embed_query(self, query: str) -> list[float]:

        vector = self.model.encode(query)

        return vector.tolist()
    
    
    
    
embedding_service = EmbeddingService()