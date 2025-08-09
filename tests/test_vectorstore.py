from app.vectorstore import TfidfVectorStore, StoredDocument


def test_vectorstore_add_and_query() -> None:
    store = TfidfVectorStore()
    n = store.add_documents(
        [
            StoredDocument(doc_id="1", text="Apples and bananas are fruits."),
            StoredDocument(doc_id="2", text="Kubernetes orchestrates containers."),
        ]
    )
    assert n == 2

    hits = store.query("What does Kubernetes do?", top_k=1)
    assert len(hits) == 1
    idx, score = hits[0]
    assert 0 <= score <= 1
    doc = store.get_document(idx)
    assert doc.doc_id == "2"


