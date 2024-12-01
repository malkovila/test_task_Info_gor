from fastapi import FastAPI, HTTPException

from db_manager import VectorDB
from serializers import SearchQuery, AddDocuments
from utils import embed_texts

app = FastAPI(title="Vector Search API")

# Инициализация базы данных
db = VectorDB()


# эндпоинт для обработки поиска схожего документа
@app.post("/search")
async def search(query: SearchQuery):
    # преобразование текста в вектор
    query_vector = await embed_texts([query.query])[0]
    # поиск
    results = await db.search(query_vector, query.limit)
    return {"results": results}

# эндпоинт для обработки добавляения документа
@app.post("/add")
async def add_documents(payload: AddDocuments):
    # проверка на добавление непустого значения
    if not payload.documents:
        raise HTTPException(status_code=400, detail="Documents list cannot be empty.")
    # преобразование текста в вектор
    vectors = await embed_texts(payload.documents)
    # добавление в бд
    await db.add_documents(payload.documents, vectors)
    return {"message": "Documents added successfully."}
