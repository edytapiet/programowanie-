from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO
import cv2
import os
import uuid
import shutil
import requests
import numpy as np

app = FastAPI()


print("Ładowanie modelu YOLO...")
model = YOLO('yolov8n.pt')
print("Model załadowany")

os.makedirs("images", exist_ok=True)
os.makedirs("processed", exist_ok=True)


def process_image(image_path: str):

    results = model(image_path, classes=0)

    people_count = 0
    output_filename = f"processed/done_{os.path.basename(image_path)}"

    for result in results:
        people_count += len(result.boxes)

        im_array = result.plot()

        cv2.imwrite(output_filename, im_array)

    return people_count, output_filename


@app.get("/")
def read_root():
    return {"message": "API działa, wejdź na /docs"}



@app.get("/detect/local")
def detect_local(file_path: str):
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Plik nie istnieje")

    count, out_path = process_image(file_path)
    return {
        "source": "local",
        "people_count": count,
        "saved_image": out_path
    }


@app.get("/detect/url")
def detect_url(image_url: str):
    try:
        response = requests.get(image_url)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Nie udało się pobrać zdjęcia")

        filename = f"images/{uuid.uuid4()}.jpg"
        with open(filename, 'wb') as f:
            f.write(response.content)


        count, out_path = process_image(filename)

        return {
            "source": "url",
            "people_count": count,
            "saved_image": out_path
        }
    except Exception as e:
        return {"error": str(e)}


@app.post("/detect/upload")
def detect_upload(file: UploadFile = File(...)):
    filename = f"images/{uuid.uuid4()}_{file.filename}"
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    count, out_path = process_image(filename)

    return {
        "source": "upload",
        "people_count": count,
        "saved_image": out_path
    }