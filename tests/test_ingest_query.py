from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_ingest_and_query() -> None:
    # Ingest a small corpus
    payload = {
        "documents": [
            {"id": "1", "text": "FastAPI is a modern web framework for Python APIs."},
            {
                "id": "2",
                "text": "Kubernetes orchestrates containerized applications for scaling and resiliency.",
            },
            {
                "id": "3",
                "text": "Vector search retrieves similar documents using embeddings or TF-IDF.",
            },
        ]
    }
    r = client.post("/ingest", json=payload)
    assert r.status_code == 200
    assert r.json()["ingested"] == 3

    # Query and expect k=2 results, with Kubernetes likely among top sources
    q = {"query": "What is Kubernetes used for?", "top_k": 2}
    r = client.post("/query", json=q)
    assert r.status_code == 200
    body = r.json()
    assert "answer" in body and isinstance(body["answer"], str)
    assert "sources" in body and isinstance(body["sources"], list)
    assert len(body["sources"]) == 2
    # At least one source should mention Kubernetes
    assert any("Kubernetes" in s["text"] for s in body["sources"])  # basic relevance check


