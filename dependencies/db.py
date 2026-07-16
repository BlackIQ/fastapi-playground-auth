# Session
from core.db import session


# Get DB Dependency
def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()
