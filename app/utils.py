from sentence_transformers import SentenceTransformer

# Инициализация модели для генерации эмбеддингов
model = SentenceTransformer('all-MiniLM-L6-v2')

async def embed_texts(texts):
    """Генерация векторного представления для текста."""
    return model.encode(texts, convert_to_tensor=True).tolist()

