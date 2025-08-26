from model import model_pipeline

from typing import Union

from fastapi import FastAPI, UploadFile
from PIL import Image

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask")
def ask(text: str, img: UploadFile):
    image = Image.open(img.file)
    return model_pipeline(image, text)

