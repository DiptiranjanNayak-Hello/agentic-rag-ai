from langchain_core.tools import tool
from app.services.retrieval_pipeline import run_retrieval_pipeline

@tool
def query_knowledge_base(query: str):
    """
    Look up specific information in the uploaded PDF documents. 
    Use this when the user asks questions about the content of the files.
    """

    context_chunks = run_retrieval_pipeline(query)

    formatted_context = "\n\n".join([
        f"Source: {c['source']} (Page {c['page']}):\n{c['text']}" 
        for c in context_chunks
    ])

    return formatted_context

tools = [query_knowledge_base]  