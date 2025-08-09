from fastapi import FastAPI

app = FastAPI(title="RAG Ops Platform")

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
