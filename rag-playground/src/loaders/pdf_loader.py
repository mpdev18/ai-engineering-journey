from pypdf import PdfReader
from langchain_core.documents import Document
from loaders.base_loader import BaseLoader

class PDFLoader(BaseLoader):
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        print(f"Loading {self.file_path} file content")
        reader = PdfReader(self.file_path)

        docs: list[Document] = []
        for page_number, page in enumerate(reader.pages):
            docs.append(
                Document(
                    page_content=page.extract_text() or "",
                    metadata={
                        "page": page_number + 1,
                        "source": self.file_path,
                        "type": "pdf"
                    }
                )
            )

        return docs