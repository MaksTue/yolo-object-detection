from ultralytics import YOLO
import os

# Директории, переданные через Docker
data_dir = '/app/data'
output_dir = '/app/results'

# Загружаем модель
model = YOLO("yolov8n.pt")

# Запускаем обучение с правильными путями
model.train(data=os.path.join(data_dir, "data.yaml"), epochs=50, imgsz=416, project=output_dir)

model.export(format='tflite', project=output_dir)