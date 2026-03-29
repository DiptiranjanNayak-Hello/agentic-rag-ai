import uuid
from app.core.embeddings import embeddings
from app.core.vectorstore import index
from app.ingestion.processor import process_pdf
import os

def run_ingestion(file_path: str):
    """
    Convert to Embeddings and Push to Pinecone.
    """

    chunks = process_pdf(file_path)
    file_name = os.path.basename(file_path)

    vectors = []

    texts = [chunk.page_content for chunk in chunks]
    embeddings_list = embeddings.embed_documents(texts)

    for i, (chunk, emb) in enumerate(zip(chunks, embeddings_list)):
        vector_id = f"{file_path}#{i}#{uuid.uuid4().hex[:6]}"

        vectors.append({
            "id": vector_id,
            "values": emb,
            "metadata": {
                "text": chunk.page_content,
                "source": file_name,
                "page": chunk.metadata.get("page", 0)
            }
        })

    batch_size = 100
    for i in range(0, len(vectors), batch_size):
        index.upsert(vectors = vectors[i: i+batch_size])

    return len(vectors)