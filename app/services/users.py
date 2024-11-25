from app.database.users import users_collection
from app.schemas.users import User
from fastapi import HTTPException

class UserService:
    @staticmethod
    async def create_user(user: User):
        existing_user = await users_collection.find_one({"email": user.email})
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        user_dict = user.dict()
        result = await users_collection.insert_one(user_dict)
        return {"id": str(result.inserted_id), "message": "User registered successfully"}

