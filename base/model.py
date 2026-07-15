# SQLAlchemy Base
from sqlalchemy.orm import DeclarativeBase

# Mixins
from base.mixins import TimestampMixin, SoftDeleteMixin


# Base Class: Model
class BaseModel(TimestampMixin, SoftDeleteMixin, DeclarativeBase):
    pass
