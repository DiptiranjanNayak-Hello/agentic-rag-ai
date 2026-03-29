from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# import os

def process_pdf(file_path: str):
    """
    Loading and Chunking text.
    Uses PyMuPDF (fitz) for speed and Recursive Splitting for quality.
    """

    # loading
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()

    # chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100,
        separators = ["\n\n", "\n", ".", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)
    return chunks