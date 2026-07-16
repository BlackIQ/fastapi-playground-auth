# Datetime
from datetime import datetime

# BaseSchema
from base import BaseSchema


# User Schema
class UserBase(BaseSchema):
    name: str
    email: str
    username: str


class UserUpdate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
