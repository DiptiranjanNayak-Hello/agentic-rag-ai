from langchain_openai import ChatOpenAI
from app.config import settings

llm = ChatOpenAI(
    model = settings.LLM_MODEL,
    temperature = 0,
    api_key = settings.OPENAI_API_KEY
)