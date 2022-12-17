"""Main"""
from fastapi import FastAPI
from uvicorn import run

from routes import auth, user

app = FastAPI()

app.include_router(router=auth.router, prefix="/auth", tags=["Auth"])
app.include_router(router=user.router, prefix="/users", tags=["Users"])


@app.get("/")
def home():
    """Home"""
    return {"Hello": "World"}


if __name__ == "__main__":
    run(app="main:app", reload=True)
