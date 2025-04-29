# 🔍 VDB Template

This is a plug-and-play vector database system built with LangChain + FAISS + Flask.  
It allows you to ingest `.txt` and `.pdf` files, chunk them into embeddings, and query them via CLI or API.

---

## 📁 Folder Structure

/data → Drop your text or PDF files here
/faiss_index → Auto-saves the vector DB here
/utils → Core vector logic (vector_tools.py)
venv/ → Local Python environment (not committed)
ingest.py → Script to load files and build vector DB
query.py → Script to search the DB from the terminal
app.py → Flask API for querying via POST request
.env → Store your OpenAI API key here

yaml
Copy
Edit

---

## 🚀 How to Use

1. Activate your virtual environment:
source venv/bin/activate

markdown
Copy
Edit

2. Add your `.txt` or `.pdf` files to `/data`

3. Ingest them into the DB:
python3 ingest.py

arduino
Copy
Edit

4. Run a test query (optional):
python3 query.py

markdown
Copy
Edit

5. Or launch the Flask API:
python3 app.py

yaml
Copy
Edit

---

## 🔐 .env Setup

Create a `.env` file with your OpenAI key:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

yaml
Copy
Edit

---

## ✅ Notes
- Uses `OpenAIEmbeddings()` — requires `tiktoken`, `openai`, `langchain`, etc.
- Change chunk size or logic inside `vector_tools.py` if needed.
