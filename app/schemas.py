from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class Document(BaseModel):
    id: Optional[str] = Field(default=None, description="Optional document id")
    text: str
    metadata: Optional[Dict[str, Any]] = None


class IngestRequest(BaseModel):
    documents: List[Document]


class IngestResponse(BaseModel):
    ingested: int


class QueryRequest(BaseModel):
    query: str
    top_k: int = 3


class QuerySource(BaseModel):
    id: Optional[str]
    text: str
    score: float


class QueryResponse(BaseModel):
    answer: str
    sources: List[QuerySource]


