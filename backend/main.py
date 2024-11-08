# fastapi-backend/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
async def read_root():
    return {"message": "Hello from FastAPI"}
