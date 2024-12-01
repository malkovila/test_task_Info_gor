from pydantic import BaseModel


class SearchQuery(BaseModel):
    query: str
    limit: int = 5


class AddDocuments(BaseModel):
    documents: list[str]
