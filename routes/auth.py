"""Auth routes"""
from fastapi import APIRouter, status

from models import User

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
)
def signup():
    """Signup"""


@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
)
def login():
    """Login"""
