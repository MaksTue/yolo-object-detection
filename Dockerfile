# Используем официальный образ Ultralytics
FROM ultralytics/ultralytics:latest

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем проект в контейнер
COPY . .

# Команда для запуска обучения
CMD ["python", "train.py"]
