from uuid import uuid4

import chromadb
from chromadb.config import Settings

class VectorDB:
    """Класс для управления векторной базой данных."""

    def __init__(self):
        self.settings = Settings(
            persist_directory="./chroma_data"
        )
        self.client = chromadb.Client(self.settings)
        self.collection = self.client.get_or_create_collection("documents")

    async def add_documents(self, documents, vectors):
        """Добавление документов в базу данных."""
        ids = [str(uuid4()) for _ in documents]
        await self.collection.add(
            documents=documents,
            embeddings=vectors,
            ids=ids
        )

    async def search(self, query_vector, limit):
        """Поиск наиболее релевантных документов."""
        results = await self.collection.query(
            query_embeddings=[query_vector],
            n_results=limit
        )
        return [{"document": doc, "score": score} for doc, score in zip(results["documents"][0], results["distances"][0])]
