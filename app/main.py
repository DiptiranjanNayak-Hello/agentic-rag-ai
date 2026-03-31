from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
from tempfile import NamedTemporaryFile
from app.ingestion.pipeline import run_ingestion
import os
from pydantic import BaseModel
from app.agents.graph import agent_executor
from app.services.schemas import ChatResponse, ChatRequest

app = FastAPI(title="Agentic RAG Service", version="1.0.0")

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


class QueryRequest(BaseModel):
    message: str
    session_id: str = "default-user"

@app.post("/query")
async def chat_with_agent(request: QueryRequest):
    config = {"configurable": {"thread_id": request.session_id}}

    inputs = {"messages": [("user", request.message)]}

    response = agent_executor.invoke(inputs)

    final_answer = response['messages'][-1].content
    return {"answer": final_answer}

@app.post("/chat", response_model = ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        inputs = {"messages": [("user", request.query)]}
        config = {"configurable": {"thread_id": request.session_id}}

        result = await agent_executor.ainvoke(inputs, config=config)

        return ChatResponse(
            answer=result["messages"][-1].content,
            sources=result.get("metadata", {}).get("source_documents", []),
            intermediate_steps=[str(m) for m in result["messages"][:-1]]
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)