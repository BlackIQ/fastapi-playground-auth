# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Settings
from core.settings import settings

# Engine
engine = create_engine(settings.postgres_url)

# Session
session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
