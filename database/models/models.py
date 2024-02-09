from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship,declarative_base
#from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(20),nullable=False)
    password = Column(String(20), nullable=False)
    task = relationship("Task",back_populates="user")

    def __repr__(self):
        return f'Username: {self.username}, Password: {self.password} Task Num: '
    

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    title = Column(String(20), nullable=False)
    priority = Column(Integer,nullable=False)
    state = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Title:{self.title}, Priority:{self.priority}, State{self.state}'
    
