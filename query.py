from utils.vector_tools import load_vector_store, query_vector_store

# 🔎 You can change this query later to test different prompts
query = "What is this database about?"

print("📂 Loading vector store...")
vectordb = load_vector_store()

print("🔍 Searching...")
results = query_vector_store(vectordb, query)

print("📝 Top Matches:")
for i, res in enumerate(results, 1):
    print(f"\nMatch {i}:\n{res}")