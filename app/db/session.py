from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=create_engine(settings.DATABASE_URL)
)
