"""Auth model"""
from pydantic import BaseModel, Field

from models.user import BaseUser, User


class PasswordMixin(BaseModel):
    """Password model"""

    password: str = Field(min_length=8, max_length=32)


class LoginUser(PasswordMixin, BaseUser):
    """Login User model"""


class RegisterUser(PasswordMixin, User):
    """Register User model"""
