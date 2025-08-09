# Work Items (Backlog and Tracking)

Status: TODO | DOING | DONE | BLOCKED | DEFERRED

## Week 1: Baseline + API
- [ ] W1-01: Scaffold FastAPI monolith with /health
- [ ] W1-02: Implement TF‑IDF vector store and /ingest
- [ ] W1-03: Implement /query returning answer + sources
- [ ] W1-04: Add pydantic schemas and minimal unit tests
- [ ] W1-05: Dockerize and run; smoke tests via curl
- [ ] W1-06: Document API (OpenAPI summary) and update README links

## Week 2: MLflow + DVC + Packaging
- [ ] W2-01: Set up MLflow tracking server (local) and log runs
- [ ] W2-02: Register baseline model in MLflow Model Registry
- [ ] W2-03: Initialize DVC; version raw and processed datasets
- [ ] W2-04: Create reproducible training script/pipeline (DVC stage)
- [ ] W2-05: pyproject + pre-commit (ruff/black) + basic type checks

## Week 3: CI + Docker + K8s
- [ ] W3-01: Multi‑stage Dockerfile for slim image
- [ ] W3-02: GitHub Actions: lint, test, build, push image
- [ ] W3-03: K8s manifests with readiness/liveness, ConfigMap/Secret
- [ ] W3-04: Kind deployment and verification script

## Week 4: Observability + Testing
- [ ] W4-01: Expose Prometheus metrics endpoint
- [ ] W4-02: Grafana dashboard JSON and provisioning
- [ ] W4-03: Structured logging + trace IDs
- [ ] W4-04: Pytest coverage ≥ 80%; load testing (k6/locust)

## Week 5: Orchestration + Gates
- [ ] W5-01: Prefect/Airflow DAG/Flow for retraining
- [ ] W5-02: Evaluation gates (NDCG/EM/F1 thresholds) block bad models
- [ ] W5-03: Auto-deploy to staging on passing gates

## Week 6: Progressive Delivery + Hardening
- [ ] W6-01: Shadow deployment
- [ ] W6-02: A/B with traffic split; online metrics collection
- [ ] W6-03: Rollback playbook + chaos test

## Nice-to-haves
- [ ] Helm chart; SOPS/Sealed Secrets
- [ ] Feature store integration; embedding upgrade
