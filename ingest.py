from vector_tools import load_documents, split_documents, create_vector_store

print("📂 Loading documents...")
docs = load_documents()

print(f"✅ Loaded {len(docs)} raw documents.")
print("✂️  Splitting into chunks...")
chunks = split_documents(docs)

print(f"✅ Created {len(chunks)} chunks.")
print("💾 Building and saving vector store...")
create_vector_store(chunks)

print("✅ All done! Vector store created and saved.")
