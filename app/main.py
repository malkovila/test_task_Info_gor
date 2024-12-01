from fastapi import FastAPI, HTTPException

from db_manager import VectorDB
from serializers import SearchQuery, AddDocuments
from utils import embed_texts

app = FastAPI(title="Vector Search API")

# Инициализация базы данных
db = VectorDB()

@app.post("/search")
async def search(query: SearchQuery):
    """Эндпоинт для поиска релевантных документов."""
    query_vector = await embed_texts([query.query])[0]
    results = await db.search(query_vector, query.limit)
    return {"results": results}


@app.post("/add")
async def add_documents(payload: AddDocuments):
    if not payload.documents:
        raise HTTPException(status_code=400, detail="Documents list cannot be empty.")
    vectors = await embed_texts(payload.documents)
    await db.add_documents(payload.documents, vectors)
    return {"message": "Documents added successfully."}
