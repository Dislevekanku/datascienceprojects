import os
import types

import pytest


fastapi = pytest.importorskip("fastapi")

# Ensure required environment variables exist before importing the app
os.environ.setdefault("OPENAI_API_KEY", "test-key")

from fastapi.testclient import TestClient

from app import main


async def _fake_run(self, messages):
    """Deterministic agent stub for testing."""
    # store the last messages for assertions if needed
    self._last_messages = messages
    return "stubbed reply"


main.agent.run = types.MethodType(_fake_run, main.agent)

client = TestClient(main.app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_chat_returns_agent_response():
    payload = {"messages": [{"role": "user", "content": "Hello"}]}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    assert response.json() == {"reply": "stubbed reply"}
    assert getattr(main.agent, "_last_messages") == payload["messages"]
