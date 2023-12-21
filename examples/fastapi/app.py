
from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def root():
    return {"message": "Hello from fastapi"}