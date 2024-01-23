from sqlalchemy import Column, String, Integer
from config.config import Base

class Task(Base):
    __tablename__ = 'task'

    title = Column(String(20), nullable=False)
    priority = Column(Integer,nullable=False)
    state = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Title:{self.title}, Priority:{self.priority}, State{self.state}'