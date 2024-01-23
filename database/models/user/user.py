from sqlalchemy import Column, String, Integer
from config.config import Base

class User(Base):
    __tablename__ = 'User'
    username = Column(String(20),nullable=False)