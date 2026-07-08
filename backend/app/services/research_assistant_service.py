from app.services.document_service import document_service
from app.services.chunk_service import chunk_service
from app.services.embedding_service import embedding_service
from app.services.vector_store_service import vector_store_service
from app.services.retriever_service import retriever_service
from app.services.prompt_builder_service import prompt_builder_service
from app.services.llm_service import llm_service
from app.schemas.answer import Answer

class ResearchAssistantService:

    def ingest_document(self, file):

        print(">>> ingest_document() called <<<")

        document = document_service.ingest_document(file)

        chunks = chunk_service.chunk(document)

        embedded_chunks = embedding_service.embed(chunks)

        vector_store_service.add(embedded_chunks)

        print("Collection count:", vector_store_service.collection.count())


        return document

       
    def ask(self, question: str):

            retrieved_chunks = retriever_service.retrieve(question)

            prompt = prompt_builder_service.build_prompt(question, retrieved_chunks)

            llm_answer = llm_service.answer(prompt)

            return Answer ( answer=llm_answer,  sources=retrieved_chunks)


research_assistant_service = ResearchAssistantService()