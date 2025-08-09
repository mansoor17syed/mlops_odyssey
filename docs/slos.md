# Service Level Objectives (SLOs)

- Availability: 99% (dev/staging)
- Latency: p95 ≤ 300 ms for short queries
- Quality: NDCG@10 ≥ 0.65 (baseline), improve over time

## Metrics
- infra: request_rate, error_rate, latency (p50/p95/p99)
- model: hit rate@k, NDCG@k, answerability
- business: query throughput, ingestion throughput
