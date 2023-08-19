from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.crud import create_user
from app.db.models import User as DBUser
from app.utils.hashing import hash_password
from pydantic import BaseModel

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


def get_db():
    """
    Get a database session.

    Returns:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create_user")
async def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new user.

    Args:
        user (UserCreate): The user data.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary containing the result message and the user ID.
    """
    user.password = hash_password(user.password)
    db_user = create_user(db, user)
    return {"message": "User created successfully", "user_id": db_user.id}


@router.post("/login")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    """
    Endpoint to handle user login.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary containing the login result message.
    """
    db_user = db.query(DBUser).filter(DBUser.username == username).first()
    if db_user and db_user.password == hash_password(password):
        return {"message": "Login successful"}
    else:
        return {"message": "Login failed"}
