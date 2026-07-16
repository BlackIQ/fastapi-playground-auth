# Datetime
from datetime import datetime, timedelta, timezone

# JWT (PyJWT)
import jwt

# Settings
from core import settings

# Secret and Algorithm
SECRET = settings.secret
ALGORITHM = settings.algorithm


def create_access_token(user_id: int) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=7)

    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    jwt_token = jwt.encode(payload=payload, key=SECRET, algorithm=ALGORITHM)

    return jwt_token
