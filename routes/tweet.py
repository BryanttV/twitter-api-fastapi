"""Tweet routes"""
from fastapi import APIRouter, status

from models import Tweet

router = APIRouter(prefix="/tweets", tags=["Tweets"])


@router.get(
    path="",
    response_model=list[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
)
def get_tweets():
    """Get tweets"""


@router.post(
    path="",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Create a tweet",
)
def create_tweet():
    """Create tweet"""


@router.delete(
    path="/{uuid}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
)
def delete_tweet():
    """Delete tweet"""


@router.patch(
    path="/{uuid}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
)
def update_tweet():
    """Update tweet"""
