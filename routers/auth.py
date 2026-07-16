# FastAPI & SQLAlchemy
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies.db import get_db  # Dependencies
from models import User  # Models
from schemas import LoginSchema, RegisterSchema, TokenSchema  # Schemas
from security.password import hash_password, verify_password  # Has Password
from security.token import create_access_token  # JWT

# FastAPI Router
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=TokenSchema)
async def register(data: RegisterSchema, db: Session = Depends(get_db)):
    email_exists = db.query(User).filter(User.email == data.email).first()

    if email_exists:
        raise HTTPException(
            status_code=409,
            detail="Email already exists",
        )

    username_exists = db.query(User).filter(User.username == data.username).first()

    if username_exists:
        raise HTTPException(
            status_code=409,
            detail="Username already exists",
        )

    user = User(name=data.name, email=data.email, username=data.username, password=hash_password(data.password))

    db.add(user)

    db.commit()
    db.refresh(user)

    access_token = create_access_token(user_id=user.id, remember=False)

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.post("/login", response_model=TokenSchema)
async def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(user_id=user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
