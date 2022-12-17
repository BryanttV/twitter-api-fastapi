"""Models"""
from datetime import datetime
from uuid import UUID, uuid4

from dateutil import tz
from pydantic import BaseModel, EmailStr, Field, PastDate


class BaseUser(BaseModel):
    """Base User model"""

    uuid: UUID = Field(default_factory=uuid4)
    email: EmailStr


class LoginUser(BaseModel):
    """Login User model"""

    password: str = Field(min_length=8, max_length=32)


class User(BaseUser):
    """User model"""

    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    birth_date: PastDate | None


class Tweet(BaseModel):
    """Tweet model"""

    uuid: UUID = Field(default_factory=uuid4)
    content: str = Field(min_length=1, max_length=280)
    created_at: datetime = Field(default=datetime.utcnow().replace(tzinfo=tz.tzutc()))
    updated_at: datetime | None
    by: User
