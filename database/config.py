import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Environ must be used in container api envs, 

USER = os.environ['DATABASE_USER']
PASSWORD = os.environ['DATABASE_PASSWORD']
HOST = os.environ['DATABASE_HOST']
DATABASE = os.environ['DATABASE']
PORT = os.environ['DATABASE_PORT']

CONN_STRING = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(CONN_STRING, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


