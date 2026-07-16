from pathlib import Path
from loaders.loader_factory import LoaderFactory
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import config

def load_documents():
    documennts: list[Document] = []

    for file in Path(config.DATA_DIR_PATH).iterdir():
        
        if file.is_file():
            loader = LoaderFactory.create(str(file))
            documennts.extend(loader.load())

    print("Document Length: ", len(documennts))
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP)

    return splitter.split_documents(documents=documennts)


