from sentence_transformers import SentenceTransformer

# Инициализация модели для генерации эмбеддингов
model = SentenceTransformer('all-MiniLM-L6-v2')

async def embed_texts(texts):
    # генерация вектора из текста
    return model.encode(texts, convert_to_tensor=True).tolist()

