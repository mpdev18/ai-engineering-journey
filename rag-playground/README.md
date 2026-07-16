# RAG Playground

A simple Retrieval-Augmented Generation (RAG) example built with Python, LangChain, Ollama, and Chroma.

## What this project does

This project demonstrates a minimal RAG workflow:

- load documents from the local data folder
- split them into smaller chunks
- create or reuse a vector database with Chroma
- retrieve relevant chunks and answer questions with an LLM

## Project structure

- `src/` - application code
  - `main.py` - interactive chat loop
  - `document_loader.py` - document loading and chunking
  - `embedder.py` - vector store creation and reuse
  - `retriever.py` - retrieval logic
  - `rag.py` - prompt and LLM answer generation
- `data/` - sample documents used for retrieval
- `requirements.txt` - Python dependencies

## Requirements

- Python 3.10+
- Ollama installed and running locally
- An embedding model and LLM available in Ollama

## Setup

1. Create and activate a virtual environment

   Windows:

   ```bash
   python -m venv .venv
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .venv\Scripts\activate
   ```

   macOS / Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app

   ```bash
   python src/main.py
   ```

4. Type a question when prompted. Type `exit` to quit.

## Notes

- The first run will create the local Chroma vector database.
- Later runs reuse the existing database automatically.
- You can remove the `.chroma_db` folder to force a rebuild.

## License

This project is for educational purposes.
