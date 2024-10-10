import shutil
from fastapi import FastAPI, File, UploadFile
import pytesseract


app = FastAPI()

 # basic third party application for ocr 
@app.post("/ocr")
def ocr(image: UploadFile = File(...)):
    filepath = "txtFile"
    with open(filepath, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return pytesseract.image_to_string(filepath, lang="eng")
