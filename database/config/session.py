from . import config as cg 
from sqlalchemy.orm import sessionmaker

def return_session():
    Session = sessionmaker(bind=cg.ENGINE)
    session = Session()
    return session


