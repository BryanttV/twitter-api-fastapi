"""Auth routes"""
import json

from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder

from models.auth import RegisterUser
from models.user import User

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
)
def signup(user: RegisterUser = Body()):
    """Signup"""
    with open("mocks/users.json", "r+", encoding="utf-8") as file:
        results: list = json.load(file)
        user_dict = jsonable_encoder(user)
        results.append(user_dict)
        file.seek(0)
        file.write(json.dumps(results))
        return user


@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
)
def login():
    """Login"""
