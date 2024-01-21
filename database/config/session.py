from . import config as cg 
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=cg.ENGINE)
session = Session()
#our session was created

