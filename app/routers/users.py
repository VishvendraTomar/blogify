from fastapi import APIRouter, HTTPException
from app.schemas.users import User
from app.services.users import UserService

router = APIRouter()

@router.post("/signup/", status_code=201)
async def signup(user: User):
    return await UserService.create_user(user)
