# FastAPI
from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user  # Dependencies
from models import User  # Models
from schemas import UserRead  # Schemas

# FastAPI Router
router = APIRouter(
    prefix="/users",
    tags=["User"]
)


@router.get("/me", response_model=UserRead)
async def me(current_user: User = Depends(get_current_user)):
    return current_user
