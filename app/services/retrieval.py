from app.core.embeddings import embeddings
from app.core.vectorstore import index

def vector_search(query: str, top_k: int = 10):
    """
    Query Pinecone for semantic matches.
    """

    query_vector = embeddings.embed_query(query)

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    retrieved_chunks = []
    for match in results['matches']:
        retrieved_chunks.append({
            "text": match["meatdata"]["text"],
            "score": match["score"],
            "page": match["metadata"].get("page"),
            "source": match["metadata"].get("source")
        })

    return retrieved_chunks