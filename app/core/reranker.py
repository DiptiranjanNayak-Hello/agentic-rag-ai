from flashrank import Ranker, RerankRequest

ranker = Ranker(model_name="ms-marco-MiniLM-L-12-v2", cache_dir="/tmp")

def rerank_documents(query: str, documents: list, top_n: int = 3):
    """
    Re-evaluate retrieved chunks using a Cross-Encoder.
    """

    passages = [
        {"id": i, "text": doc["text"], "meta": doc}
        for i, doc in enumerate(documents)
    ]

    rerank_request = RerankRequest(query = query, passages=passages)
    results = ranker.rerank(rerank_request)

    return [res["meta"] for res in results[:top_n]]