from app.db.models import User


def create_user(db, user):
    """
    Create a new user in the database.

    Args:
        db (Session): The database session.
        user (UserCreate): The user data.

    Returns:
        User: The created user.
    """
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
