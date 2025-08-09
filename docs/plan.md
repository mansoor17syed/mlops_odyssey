# LLM RAG Ops Platform — Mastery Plan (6 Weeks)

## Objective
Build a production-grade Retrieval-Augmented Generation (RAG) API and end-to-end MLOps system: reproducible data and training pipelines, experiment tracking, model registry, CI/CD to Kubernetes, observability, scheduled retraining, and progressive delivery.

## Phases
1. Data + Baseline Retrieval (monolith)
2. API Serving (monolith)
3. Experiment Tracking + Data Versioning (MLflow + DVC)
4. Packaging + Testing (pyproject, pre-commit, pytest)
5. Containers + CI (Docker, GitHub Actions)
6. Kubernetes Deploy (kind, Kustomize/Helm)
7. Observability (Prometheus, Grafana, OTel)
8. Retraining Orchestration (Prefect/Airflow) with quality gates
9. Progressive Delivery (shadow/A/B/canary)
10. Scale/Split services only if justified by load/ownership

## SLOs (Initial)
- Availability ≥ 99% (dev/staging)
- p95 latency ≤ 300 ms for short queries (1 replica)
- Retrieval quality: baseline NDCG@10 ≥ 0.65

## Weekly Schedule (Strict)
### Week 1 — Baseline + API (monolith)
- Deliverables: /health, /ingest, /query; TF‑IDF baseline; container build; smoke tests
- Acceptance: From clean clone → container runs; query returns sources; tests pass

### Week 2 — MLflow + DVC + Packaging
- Deliverables: MLflow experiments + model registry; DVC pipeline; pyproject; pre-commit
- Acceptance: All runs tracked; data versioned; pre-commit clean

### Week 3 — CI + Docker + K8s Bootstrap
- Deliverables: Multi-stage Dockerfile; CI pipeline (tests, build, push); K8s manifests (readiness/liveness)
- Acceptance: CI green; image pushed; pod healthy in kind

### Week 4 — Observability + Testing Depth
- Deliverables: Prometheus metrics; Grafana dashboard; structured logs; coverage ≥ 80%; load test report
- Acceptance: p50/p95/p99 visible; alerting for error‑rate; SLO respected under load

### Week 5 — Retraining Pipeline + Gates
- Deliverables: Prefect/Airflow flow (ingest→train→eval→register); auto-promotion to staging on passing gates
- Acceptance: Scheduled retrain runs; manual promotion to prod

### Week 6 — Progressive Delivery + Hardening
- Deliverables: Shadow→A/B rollout; rollback playbook; security scans; final demo + docs
- Acceptance: Traffic split verified; rollback tested; checks green; demo recorded

## Daily Discipline
- Commit daily with passing tests
- Update progress log and learning journal
- Track experiments and decisions in MLflow and docs
