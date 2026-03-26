from fastapi import FastAPI

app = FastAPI(title="Agentic RAG Pipeline", version="1.0.0")

@app.get("/health")
def health():
    """Check if the server is alive."""
    return {
        "status": "ok",
        "message": "Agentic RAG Backend is Online"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)