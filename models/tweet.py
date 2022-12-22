"""Tweet model"""
from datetime import datetime
from uuid import UUID, uuid4

from dateutil import tz
from pydantic import BaseModel, Field

from models.user import User


class Tweet(BaseModel):
    """Tweet model"""

    uuid: UUID = Field(default_factory=uuid4)
    content: str = Field(min_length=1, max_length=280)
    created_at: datetime = Field(default=datetime.utcnow().replace(tzinfo=tz.tzutc()))
    updated_at: datetime | None
    by: User
