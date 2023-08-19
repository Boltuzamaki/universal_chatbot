from fastapi import APIRouter
from database import add_user, get_user
from models import User
from utils.hashing import hash_password

router = APIRouter()

@router.post("/users")
async def create_user(user: User):
    hashed_password = hash_password(user.password)
    add_user(user.username, user.email, hashed_password)
    return {"message": "User created successfully"}

@router.post("/users/login")
async def login(username: str, password: str):
    hashed_password = hash_password(password)
    user = get_user(username, hashed_password)
    if user:
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}