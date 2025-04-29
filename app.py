from flask import Flask, request, jsonify
from vector_tools import load_vector_store, query_vector_store  # Updated import

app = Flask(__name__)
vectordb = load_vector_store()

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    query = data.get("query", "")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = query_vector_store(vectordb, query)
    return jsonify({"matches": results})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)