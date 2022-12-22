"""Main"""
from fastapi import FastAPI
from uvicorn import run

from routes import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    """Home"""
    return {"Hello": "World"}


if __name__ == "__main__":
    run(app="main:app", reload=True)
