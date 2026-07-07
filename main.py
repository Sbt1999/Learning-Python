from fastapi import FastAPI
from fastapi import UploadFile, File
# It creates one FastApi() application
app = FastAPI()

# Register a GET endpoint for the root URL
@app.get("/")
def read_root():
    return {"message": "AI Interview Backend is running"}
