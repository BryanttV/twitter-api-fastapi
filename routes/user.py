"""User routes"""
from fastapi import APIRouter, status

from models import User

router = APIRouter()


@router.get(
    path="",
    response_model=list[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
)
def get_users():
    """Get users"""


@router.get(
    path="/{uuid}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
)
def get_user():
    """Get user"""


@router.delete(
    path="/{uuid}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
)
def delete_user():
    """Delete user"""


@router.patch(
    path="/{uuid}",
    response_model=User,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Update a user",
)
def update_user():
    """Update user"""
