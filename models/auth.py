"""Auth model"""
from pydantic import Field

from models import BaseUser


class LoginUser(BaseUser):
    """Login User model"""

    password: str = Field(min_length=8, max_length=32)
