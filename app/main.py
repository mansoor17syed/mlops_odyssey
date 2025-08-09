from typing import List
from fastapi import FastAPI
from app.schemas import (
    IngestRequest,
    IngestResponse,
    QueryRequest,
    QueryResponse,
    QuerySource,
)
from app.vectorstore import TfidfVectorStore, StoredDocument

app = FastAPI(
    title="RAG Ops Platform",
    description=(
        "Retrieval-Augmented Generation API. Ingest documents and query them. "
        "This is the Week 1 baseline using TF-IDF retrieval."
    ),
    version="0.1.0",
)
_vector_store = TfidfVectorStore()

@app.get("/health", summary="Health check", tags=["system"])
def health() -> dict:
    return {"status": "ok"}


@app.post(
    "/ingest",
    response_model=IngestResponse,
    summary="Ingest documents",
    description=(
        "Add one or more documents to the in-memory vector index (TF-IDF). "
        "Rebuilds the index on each call for simplicity."
    ),
    tags=["core"],
)
def ingest(payload: IngestRequest) -> IngestResponse:
    docs: List[StoredDocument] = [
        StoredDocument(doc_id=d.id, text=d.text) for d in payload.documents
    ]
    count = _vector_store.add_documents(docs)
    return IngestResponse(ingested=count)


@app.post(
    "/query",
    response_model=QueryResponse,
    summary="Query documents",
    description=(
        "Return the top-k documents most similar to the query using cosine similarity over TF-IDF vectors. "
        "The answer field returns the top document text as a simple baseline."
    ),
    tags=["core"],
)
def query(payload: QueryRequest) -> QueryResponse:
    matches = _vector_store.query(payload.query, top_k=payload.top_k)
    sources: List[QuerySource] = []
    for idx, score in matches:
        d = _vector_store.get_document(idx)
        sources.append(QuerySource(id=d.doc_id, text=d.text, score=score))
    answer = sources[0].text if sources else ""
    return QueryResponse(answer=answer, sources=sources)
