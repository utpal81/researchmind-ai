from app.services.research_assistant_service import research_assistant_service


def test_ask_returns_prompt():

    answer = research_assistant_service.ask(
        "What is this document about?"
    )

    assert isinstance(answer, str)
    assert len(answer) > 0