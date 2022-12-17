"""Main"""
from fastapi import FastAPI
from uvicorn import run

app = FastAPI()


@app.get("/")
def home():
    """Home"""
    return {"Hello": "World"}


if __name__ == "__main__":
    run(app="main:app", reload=True)
