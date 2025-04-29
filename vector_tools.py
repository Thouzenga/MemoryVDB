import os
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

DATA_FOLDER = "Data"
INDEX_FOLDER = "Faiss_index"

def load_documents():
    docs = []
    for file in os.listdir(DATA_FOLDER):
        path = os.path.join(DATA_FOLDER, file)
        if file.endswith(".txt"):
            docs.extend(TextLoader(path).load())
        elif file.endswith(".pdf"):
            docs.extend(PyPDFLoader(path).load())
    return docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(INDEX_FOLDER)

def load_vector_store():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(INDEX_FOLDER, embeddings, allow_dangerous_deserialization=True)

def query_vector_store(vectorstore, query):
    results = vectorstore.similarity_search(query)
    return [doc.page_content for doc in results]
