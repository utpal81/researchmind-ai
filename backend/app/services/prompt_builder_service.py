from app.schemas.retrieval import RetrievedChunk


class PromptBuilderService:

    def build_prompt(
        self,
        question: str,
        retrieved_chunks: list[RetrievedChunk] ) -> str:

        context = ""

        for chunk in retrieved_chunks:

            context += (
                f"Page {chunk.page_number}\n"
                f"{chunk.text}\n\n"
            )

        prompt = f"""
                You are ResearchMind AI.

                Answer ONLY using the supplied context.

                If the answer is not found in the context,
                say that you could not find it.

                Context
                --------

                {context}

                Question
                --------

                {question}

                Answer
                --------
                """

        return prompt


prompt_builder_service = PromptBuilderService()