# Datetime

# BaseSchema
from base import BaseSchema


# Login Schema
class LoginSchema(BaseSchema):
    email: str
    password: str


# Register Schema
class RegisterSchema(LoginSchema):
    name: str
    username: str
