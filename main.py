from fastapi import FastAPI
from fastapi import UploadFile, File
from pathlib import Path
import shutil
# It creates one FastApi() application
app = FastAPI()

# Register a GET endpoint for the root URL
@app.get("/")
def read_root():
    return {"message": "AI Interview Backend is running"}

@app.post("/upload")
def upload_resume(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type" : file.content_type
    }

# In the next step I will create upload api so that it will save the pdf in uploads folder
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/fileUpload")
def upload_resum(file: UploadFile = File(...)):
    destination = UPLOAD_DIR / file.filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return {
        "message": "Resume uploaded successfuly",
        "filename": file.filename
    }