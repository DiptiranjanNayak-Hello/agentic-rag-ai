from pinecone.grpc import PineconeGRPC as Pinecone
from app.config import settings

pc = Pinecone(api_key=settings.PINECONE_API_KEY)
index = pc.Index(settings.PINECONE_INDEX_NAME)