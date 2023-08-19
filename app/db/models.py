from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from app.core.config import settings

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
