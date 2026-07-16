from pathlib import Path
from langchain_core.documents import Document
from loaders.base_loader import BaseLoader

class TextLoader(BaseLoader):
    def __init__(self, file_path:str):
        self.file_path = file_path

    def load(self):
       print(f"Loading {self.file_path} file content")
       text = Path(self.file_path).read_text(encoding="utf-8")

       return  [
        Document(
            page_content=text,
            metadata={"source": self.file_path, "type": "txt"}
        )
    ]