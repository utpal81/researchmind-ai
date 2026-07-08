from app.services.research_assistant_service import research_assistant_service


def test_ask_returns_prompt():

    response = research_assistant_service.ask(
        "What is this document about?"
    )

    assert response.answer !=""
    assert len(response.sources) > 0