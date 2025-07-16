import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

CHROMA_DB_DIR = "./chroma_db_multimodal"

def embed_and_store(raw_text: str):
    """
    Given raw text (e.g., extracted from image via OCR), split it, embed it, and save to Chroma DB.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    documents = text_splitter.create_documents([raw_text])

    embeddings_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings_function,
        persist_directory=CHROMA_DB_DIR
    )
    return vectorstore


def load_or_create_db():
    """
    Load existing Chroma DB if it exists, otherwise returns None.
    """
    if not os.path.exists(CHROMA_DB_DIR):
        os.makedirs(CHROMA_DB_DIR)
        return None

    embeddings_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
    return Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings_function
    )
