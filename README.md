# RAG Ops Platform

Production-grade Retrieval-Augmented Generation API. Week 1 baseline: ingest documents and query them using TF‑IDF retrieval.

## Purpose
- Ground LLM-style answers in your own documents to reduce hallucinations
- Serve a clean API that we will productionize with tracking, CI/CD, and K8s

## Quick Start
```bash
docker build -t rag-ops-platform:dev .
docker run -p 8000:8000 rag-ops-platform:dev
curl -s http://localhost:8000/health
```

API docs available at /docs when the container is running.

## Repo layout
- app/: FastAPI app and core logic
- tests/: unit tests
- Dockerfile, requirements.txt, pytest.ini

## Status
Week 1 — Baseline + API (in progress)
