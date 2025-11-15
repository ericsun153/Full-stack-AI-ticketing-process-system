"""RAG (Retrieval-Augmented Generation) utilities.

Includes:
- Lightweight text chunking
- Pluggable embeddings (SentenceTransformers if available, else hashing fallback)
- ChromaDB persistent vector store helpers
"""

