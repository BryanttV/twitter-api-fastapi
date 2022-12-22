"""User model"""
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field, PastDate


class BaseUser(BaseModel):
    """Base User model"""

    uuid: UUID = Field(default_factory=uuid4)
    email: EmailStr


class User(BaseUser):
    """User model"""

    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    birth_date: PastDate | None
