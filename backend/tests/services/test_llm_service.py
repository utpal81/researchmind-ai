from app.services.llm_service import llm_service


def test_llm_answer():

    answer = llm_service.answer(
        "Reply with only the word Hello."
    )

    assert answer.strip() == "Hello"