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

                Use ONLY the supplied context.

                If the answer is not completely supported
                by the supplied context,

                respond exactly with:

                "I couldn't find the answer in the uploaded documents."

                Do not use outside knowledge.

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