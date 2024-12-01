# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения
COPY . .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт, который будет прослушивать FastAPI
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
