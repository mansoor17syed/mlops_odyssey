from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class StoredDocument:
    doc_id: Optional[str]
    text: str


class TfidfVectorStore:
    """A minimal in-memory vector store using TF-IDF + cosine similarity.

    This is a simple baseline to make the system functional before we add
    dense embeddings. It keeps documents in memory and recomputes the TF-IDF
    matrix on each ingest for simplicity.
    """

    def __init__(self) -> None:
        self._vectorizer = TfidfVectorizer(stop_words="english")
        self._matrix = None  # type: ignore[var-annotated]
        self._documents: List[StoredDocument] = []

    def add_documents(self, documents: List[StoredDocument]) -> int:
        self._documents.extend(documents)
        corpus = [d.text for d in self._documents]
        self._matrix = self._vectorizer.fit_transform(corpus)
        return len(documents)

    def query(self, query_text: str, top_k: int = 3) -> List[Tuple[int, float]]:
        if not self._documents:
            return []
        assert self._matrix is not None
        q_vec = self._vectorizer.transform([query_text])
        sims = cosine_similarity(q_vec, self._matrix).ravel()
        top_idx = np.argsort(-sims)[:top_k]
        return [(int(i), float(sims[i])) for i in top_idx]

    def get_document(self, index: int) -> StoredDocument:
        return self._documents[index]


