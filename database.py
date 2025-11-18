from sqlalchemy.orm import declarative_base , sessionmaker
from sqlalchemy import create_engine 
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')


# DATABASE_URL = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
DATABASE_URL = 'sqlite:///./users.db'
# print(DATABASE_URL)
Base = declarative_base()
engine = create_engine(DATABASE_URL)
session_m = sessionmaker(autocommit=False , autoflush=False , bind=engine)

def get_db():
    session = session_m()
    try:
        yield session
    finally:
        session.close()