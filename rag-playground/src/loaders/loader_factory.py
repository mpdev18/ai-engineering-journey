from pathlib import Path

from loaders.text_loader import TextLoader
from loaders.pdf_loader import PDFLoader

class LoaderFactory:

    @staticmethod
    def create(file_path: str):
        extension = Path(file_path).suffix.lower()

        mapping = {
            ".txt" : TextLoader,
            ".pdf": PDFLoader,
        }

        loader = mapping.get(extension)

        if loader is None:
            raise ValueError(f"Unsupported file type: {extension}")
        
        return loader(file_path)