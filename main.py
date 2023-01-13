from fastapi import FastAPI, File, UploadFile
import os
from parser.extractor import *

app = FastAPI()

@app.get("/test")
def hello():
  return {"Hello world!"}

@app.post("/extractor")
async def create_upload_file(file: UploadFile):
    path = os.path.join(os.getcwd(), "pdf_files")
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = os.path.join(path, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    parsedData = extractor(file_path)
    os.remove(file_path)
    return {"exams": parsedData}