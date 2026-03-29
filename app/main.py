from fastapi import FastAPI, UploadFile, File
import shutil
from tempfile import NamedTemporaryFile
from app.ingestion.pipeline import run_ingestion
import os

app = FastAPI(title="Agentic RAG Pipeline", version="1.0.0")

@app.get("/health")
def health():
    """Check if the server is alive."""
    return {
        "status": "ok",
        "message": "Agentic RAG Backend is Online"
    }

@app.post("/ingest")
def ingest_file(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF files are allowed for now! We'll be updating the features soon for other files too. Thank you for your patience!!!"}

    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    try:
        total_vectors = run_ingestion(tmp_path)
        return {
            "message": "Ingestion Successful",
            "file": file.filename,
            "chunks_created": total_vectors
        }
    
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)