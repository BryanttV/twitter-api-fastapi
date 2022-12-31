"""Auth routes"""
from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder

from common import utils
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
    user_dict = jsonable_encoder(user)
    utils.create_mock(route="mocks/users.json", data=user_dict)
    return user_dict


@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
)
def login():
    """Login"""
