from uuid import uuid4

import chromadb
from chromadb.config import Settings

# класс для работы с векторной базой данных
class VectorDB:
    def __init__(self):
        # установка настроек для бд
        self.settings = Settings(
            persist_directory="./chroma_data"
        )
        # объявление клиента
        self.client = chromadb.Client(self.settings)
        self.collection = self.client.get_or_create_collection("documents")


    # добавление документа
    async def add_documents(self, documents, vectors):
        # генерация id для документа
        ids = [str(uuid4()) for _ in documents]
        await self.collection.add(
            documents=documents,
            embeddings=vectors,
            ids=ids
        )

    # поиск максимально схожего документа
    async def search(self, query_vector, limit):
        # внутри self.collection.query уже включен поиск по косинусному сходству
        results = await self.collection.query(
            query_embeddings=[query_vector],
            n_results=limit
        )
        return [{"document": doc, "score": score} for doc, score in zip(results["documents"][0], results["distances"][0])]
