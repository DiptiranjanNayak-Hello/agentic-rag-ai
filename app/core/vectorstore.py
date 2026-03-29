from pinecone.grpc import PineconeGRPC as Pinecone
from app.config import settings

# Creates a client object
# Authenticates with Pinecone using your API key
pc = Pinecone(api_key=settings.PINECONE_API_KEY)
index = pc.Index(settings.PINECONE_INDEX_NAME)