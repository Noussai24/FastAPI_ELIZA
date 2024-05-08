from fastapi import FastAPI
from app.api.v1.user import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Hello"}

app.include_router(router)