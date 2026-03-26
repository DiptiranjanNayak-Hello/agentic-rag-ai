import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str 
    PINECONE_API_KEY: str 

    PINECONE_INDEX_NAME: str = os.getenv("PINECONE_INDEX_NAME", "agentic-rag")

    LLM_MODEL: str = "gpt-4o"
    EMBEDDING_MODEL: str = "text-embedding-3-small"

settings = Settings()