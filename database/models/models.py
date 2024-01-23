from sqlalchemy import Column, String, Integer
from config.config import Base

class User(Base):
    __tablename__ = 'User'
    username = Column(String(20),nullable=False)
    password = Column(String(20), nullable=False)

    def __repr__(self):
        return f'Username: {self.username}, Password: {self.password} Task Num: '
    

class Task(Base):
    __tablename__ = 'task'

    title = Column(String(20), nullable=False)
    priority = Column(Integer,nullable=False)
    state = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Title:{self.title}, Priority:{self.priority}, State{self.state}'
'''    
class Employe(Base):
    __tablename__ = 'employe'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    cpf = Column(String(11),nullable=False)
    salary = Column(Float, nullable=False)
    supervisor = relationship("Supervisor", back_populates="employe")
    manager = relationship("Manager", back_populates="employe")
    operator = relationship("Operator", back_populates="employe")

class Manager(Base):
    __tablename__ = 'manager'
    id = Column(Integer, primary_key=True)
    id_employe = Column(Integer, ForeignKey('employe.id'))
    unit = Column(String(30), nullable=False)
    employe = relationship("Employe", back_populates="manager")
'''