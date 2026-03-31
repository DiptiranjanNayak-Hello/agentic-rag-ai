from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import settings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# embeddings = OpenAIEmbeddings(
#     model = settings.EMBEDDING_MODEL,
#     api_key = settings.OPENAI_API_KEY
# )