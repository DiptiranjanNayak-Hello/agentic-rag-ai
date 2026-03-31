from app.services.retrieval import vector_search
from app.core.reranker import rerank_documents

def run_retrieval_pipeline(query: str):
    """
    query -> vector search -> rerank -> top context.
    """

    initial_chunks = vector_search(query, top_k=10)
    final_context = rerank_documents(query, initial_chunks, top_n = 3)

    return final_context