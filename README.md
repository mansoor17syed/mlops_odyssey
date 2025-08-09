# LLM RAG Ops Platform — Production-Grade MLOps Project

## Goal
Build a production-grade Retrieval-Augmented Generation (RAG) API with full MLOps: reproducible data+training pipelines, experiment tracking, model registry, CI/CD to Kubernetes, progressive delivery (shadow/A/B), and model/infrastructure observability.

## Hiring Story
- You can ship reliable ML systems end-to-end: data → training → evaluation → serving → deployment → monitoring → iteration.
- Clear SLOs, measurable quality gates, and automated promotion/rollback.

## Phases (incremental; start monolith, split later if needed)
1) Data + baseline model (monolith)
2) API serving (monolith)
3) Experiment tracking + data versioning (MLflow + DVC)
4) Packaging + testing (pyproject/pre-commit/pytest)
5) Containers + CI (Docker, GitHub Actions)
6) K8s deploy (kind, Kustomize/Helm)
7) Observability (Prometheus/Grafana/OTel)
8) Retraining pipeline (Prefect/Airflow) with gates
9) Progressive delivery (shadow/A/B/canary)
10) Scale and split (only if justified)

## 6-Week Schedule (strict)
- Week 1 — Data, baseline, single API
  - Deliverables: dataset, baseline retriever/LLM config, /health and /predict (or /query) endpoint, unit+smoke tests, README
  - Acceptance: Reproducible run from clean clone; API returns correct schema; tests pass locally
- Week 2 — MLflow + DVC + packaging
  - Deliverables: MLflow experiments + model registry; DVC pipeline; pyproject; pre-commit
  - Acceptance: All experiments tracked; data versioned; pre-commit clean
- Week 3 — CI + Docker + K8s bootstrap
  - Deliverables: Multi-stage Dockerfile; CI pipeline (tests, build, push); K8s manifests
  - Acceptance: CI green; image pushed; pod healthy with readiness/liveness
- Week 4 — Observability + testing depth
  - Deliverables: Prometheus scraping; Grafana dashboard; structured logs; coverage ≥ 80%; load test report
  - Acceptance: p50/p95/p99 latency visible; alerting on error rate; SLO within limits
- Week 5 — Retraining pipeline + gates
  - Deliverables: Orchestration flow (ingest→train→eval→register); auto-promotion to staging if tests pass
  - Acceptance: Scheduled retrain; manual prod promotion after review
- Week 6 — Progressive delivery + polish
  - Deliverables: Shadow→A/B rollout; rollback playbook; security scans; final demo + docs + diagrams
  - Acceptance: Traffic split verified; rollback tested; final presentation recorded

## SLOs (initial)
- Availability ≥ 99% (dev/staging via kind)
- p95 latency ≤ 300 ms for short queries (local single replica)
- Correctness: baseline NDCG@10 ≥ 0.65 on evaluation set

## Tooling Stack (introduce when needed)
- Core: Python 3.11 (containerized), FastAPI
- RAG: sentence-transformers for embeddings, FAISS/Chroma for vector store; later Hugging Face/Inference API for LLM
- Tracking: MLflow; DVC
- Orchestration: Prefect or Airflow (Week 5)
- Infra: Docker, Kubernetes (kind), Kustomize/Helm
- CI/CD: GitHub Actions
- Observability: Prometheus, Grafana, OpenTelemetry, Loki
- Quality: pytest, ruff/black, mypy (optional), great_expectations

## Week 1 Plan (detailed)
Day 1:
- Scaffold repo (this commit)
- Implement /health endpoint
- Add requirements.txt, Dockerfile, .gitignore
- Write architecture sketch and SLOs in README

Day 2:
- Implement minimal RAG interfaces: in-memory vector index with FAISS/Chroma stub
- Endpoints: /ingest (accepts documents), /query (returns answer + sources)
- Add pydantic request/response schemas; add unit tests

Day 3:
- Add evaluation harness with a small QA set
- Track baseline metrics locally (printed); document baseline targets

Acceptance (Week 1):
- From clean clone: docker build + run → /health OK
- /ingest and /query work on small sample; smoke tests green

## Strictness & Process
- Daily: push code + design note; tests green
- Weekly: 3–5 min demo; checklist complete; short postmortem
- Non-negotiables: reproducibility, tracking, observability

## Next
- Implement minimal FastAPI app (monolith) with /health now.
