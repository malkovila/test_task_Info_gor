from pydantic import BaseModel

# сериалайзер для функции поиска документа
class SearchQuery(BaseModel):
    query: str
    limit: int = 5

# сериалайзер для функции добавления документа
class AddDocuments(BaseModel):
    documents: list[str]
