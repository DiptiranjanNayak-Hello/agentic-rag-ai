import os
from dotenv import load_dotenv
# import fitz
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()

def ingest_pdf(file_path: str):
    """
    Takes a path to a PDF, chunks it, and uploads to Pinecone.
    """

    loader = PyMuPDFLoader(file_path)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )

    docs = text_splitter.split_documents(data)