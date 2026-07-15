# SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

# BaseModel
from base import BaseModel


# User Model
class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )
    name: Mapped[str] = mapped_column(
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        nullable=False
    )
    username: Mapped[str] = mapped_column(
        nullable=False
    )
    password: Mapped[str] = mapped_column(
        nullable=False
    )
