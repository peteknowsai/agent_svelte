# agents-python/tests/test_agents_app.py
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from fastapi.testclient import TestClient
import agents_app

# dummy class to stand in for ResponseTextDeltaEvent
class DummyData:
    def __init__(self, delta):
        self.delta = delta

class DummyEvent:
    def __init__(self, type, data):
        self.type = type
        self.data = data

class DummyStreamResult:
    def __init__(self, events):
        self._events = events

    async def stream_events(self):
        for e in self._events:
            yield e

class DummySyncResult:
    def __init__(self, final_output):
        self.final_output = final_output

@pytest.fixture(autouse=True)
def patch_event_type_and_env(monkeypatch):
    # have agents_app treat DummyData as the ResponseTextDeltaEvent
    monkeypatch.setattr(agents_app, "ResponseTextDeltaEvent", DummyData)
    # avoid needing a real OpenAI key
    monkeypatch.setenv("OPENAI_API_KEY", "test")

def test_stream_agent(monkeypatch):
    events = [
        DummyEvent("raw_response_event", DummyData("Hello")),
        DummyEvent("raw_response_event", DummyData(" World")),
        DummyEvent("other_event",      DummyData("Ignored")),
    ]
    monkeypatch.setattr(
        agents_app.Runner,
        "run_streamed",
        lambda agent, input=None: DummyStreamResult(events),
    )

    client = TestClient(agents_app.app)
    resp = client.post("/api/agent/stream", json={"input": "hi"})

    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/event-stream")

    body = resp.content.decode()
    assert "data: Hello\n\n" in body
    assert "data:  World\n\n" in body
    assert "Ignored" not in body

def test_cli_main(monkeypatch, capsys):
    monkeypatch.setattr(
        agents_app.Runner,
        "run_sync",
        lambda agent, input=None: DummySyncResult("foo output"),
    )
    monkeypatch.setattr(sys, "argv", ["agents_app.py", "xyz"])
    agents_app.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "foo output"
