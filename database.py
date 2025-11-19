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


DATABASE_URL = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
# DATABASE_URL = 'sqlite:///./users.db'
# print(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

session_m = sessionmaker(autocommit=False , autoflush=False , bind=engine)

