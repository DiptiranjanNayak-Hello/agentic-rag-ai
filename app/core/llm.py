# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from app.config import settings

llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0,
    api_key=settings.GROQ_API_KEY
)

# llm = ChatOpenAI(
#     model = settings.LLM_MODEL,
#     temperature = 0,
#     api_key = settings.OPENAI_API_KEY
# )