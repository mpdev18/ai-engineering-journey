from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import config

def get_retriever():
    embeddings = OllamaEmbeddings(model=config.EMBEDDING_MODEL)
    
    db = Chroma(
        persist_directory=config.CHROMA_DB_PATH,
        embedding_function=embeddings
    )

    return db.as_retriever(
        search_kwargs={"k": config.SEARCH_KWARGS}
    )