from pathlib import Path
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import config


def db_exists() -> bool:
    db_path = Path(config.CHROMA_DB_PATH)
    return db_path.exists() and any(db_path.iterdir())

def create_vectorstore(documents:list[Document]):
    embeddings = OllamaEmbeddings(model=config.EMBEDDING_MODEL)

    if db_exists():
        return Chroma(
            persist_directory=config.CHROMA_DB_PATH,
            embedding_function=embeddings
        )

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=config.CHROMA_DB_PATH
    )

    return vectorstore