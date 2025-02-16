# Детекция объектов с YOLO и Docker

Этот репозиторий демонстрирует, как обучить модель YOLOv8 для детекции объектов на кастомном датасете. Тестовая модель(лежит в results) предназначена для обнаружения **зубных щеток**, **тюбиков зубной пасты** и **мыла**.

## Быстрый старт

Следуйте этим шагам, чтобы клонировать проект, настроить окружение с помощью Docker и обучить модель YOLOv8.

### 1. Клонирование репозитория

Сначала клонируйте репозиторий на ваш локальный компьютер:

```bash
git clone https://github.com/MaksTue/yolo-object-detection.git
cd yolo-object-detection
```

### 2. Загрузка датасета

Можно использовать код из datasetDownloadAndExportModel.ipynb
Скачайте датасет с [Roboflow: Toothbrushes, Toothpaste, and Soap](https://universe.roboflow.com/lab31/toothbrushes-toothpaste-soap).



### 3. Построение Docker образа

Первым шагом необходимо построить Docker образ. Для этого выполните команду в корневой директории проекта, где находится Dockerfile:

```bash
docker build -t yolo-object-detection .
```

Далее запускаем контейнер с обучением
```bash
docker run --ipc=host --gpus all -v /path/to/your/dataset:/app/data -v /path/to/your/results:/app/results yolo-object-detection
```
Результат обучения будет в папке results/
### 4. Экспорт и тест
В datasetDownloadAndExportModel.ipynb есть пример экспорта в tflite формат

После экспорта можно воспользоваться этим [репозиторием](https://github.com/surendramaran/YOLO/tree/main/YOLOv8-Object-Detector-Android-Tflite) чтобы проверить работу на мобильном устройстве
