"""User routes"""
import json

from fastapi import APIRouter, status

from models.user import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    path="",
    response_model=list[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
)
def get_users():
    """Get users"""
    with open("mocks/users.json", "r+", encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data


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
    status_code=status.HTTP_200_OK,
    summary="Update a user",
)
def update_user():
    """Update user"""
