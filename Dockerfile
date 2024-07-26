# Используем базовый образ с Python
FROM python:3.9-slim

# Установка необходимых системных пакетов
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Копируем исходный код приложения в образ
COPY . /app

# Указываем рабочую директорию
WORKDIR /app

# Установка зависимостей приложения
RUN pip install -r requirements.txt

# Команда для запуска вашего приложения на порту 8000
CMD ["python", "main.py"]

# Открываем порт 8000 для внешнего доступа
EXPOSE 8000

