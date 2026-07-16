# JWT
import jwt
# FastAPI & SQLAlchemy
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import PyJWTError
from sqlalchemy.orm import Session

from core import settings  # Settings
from dependencies.db import get_db  # Dependencies
from models import User  # Models

# Secret and Algorithm
SECRET = settings.secret
ALGORITHM = settings.algorithm

# OAuth2 Schema
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid or expired token",
    headers={"WWW-Authenticate": "Bearer"},
)


# Get Current User Dependency
def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    try:
        # Decode the token
        payload = jwt.decode(
            token,
            SECRET,
            algorithms=[ALGORITHM],
        )
    except PyJWTError:
        # We have an error here
        raise credentials_exception

    # Get User ID from payload
    user_id: int = payload.get("sub")
    if user_id is None:
        raise credentials_exception

    # Get User from DB
    user = db.get(User, user_id)

    # User is not found
    if user is None:
        raise credentials_exception

    return user
