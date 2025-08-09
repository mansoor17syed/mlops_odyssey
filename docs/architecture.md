# Architecture (Initial → Evolving)

- Week 1: Monolith FastAPI app with in-process vector index (TF‑IDF)
- Week 2: MLflow tracking + DVC pipeline; local artifacts
- Week 3: Containerized service; K8s manifests; readiness/liveness
- Week 4: Observability: Prometheus metrics, Grafana dashboards, logs
- Week 5: Orchestration for retraining; evaluation gates
- Week 6: Progressive delivery (shadow/A/B), rollback

Links: see plan.md, slos.md, work-items.md

## Components (Week 1)
- Client (curl/TestClient)
- FastAPI app (`app.main`)
- Vector store (`app.vectorstore.TfidfVectorStore`)
- Schemas (`app.schemas`)

## Component Diagram
```mermaid
graph TD
  C[Client] -->|HTTP| A[FastAPI App]
  A -->|/ingest| V[TfidfVectorStore]
  A -->|/query| V
  V --> M[In-memory TF-IDF matrix]
```

## Sequence — Ingest
```mermaid
sequenceDiagram
  participant C as Client
  participant A as FastAPI
  participant V as TfidfVectorStore
  C->>A: POST /ingest {documents}
  A->>V: add_documents(docs)
  V->>V: fit_transform(corpus)
  V-->>A: count
  A-->>C: {ingested: count}
```

## Sequence — Query
```mermaid
sequenceDiagram
  participant C as Client
  participant A as FastAPI
  participant V as TfidfVectorStore
  C->>A: POST /query {query, top_k}
  A->>V: query(query, k)
  V->>V: transform(query) + cosine_similarity
  V-->>A: [(idx, score)...]
  A->>A: build sources + answer
  A-->>C: {answer, sources}
```
