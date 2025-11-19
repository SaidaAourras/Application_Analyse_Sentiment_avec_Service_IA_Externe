from database import Base
from sqlalchemy import Column , Integer , String
from pydantic import BaseModel
# from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
# from passlib.context import CryptContext
# from pwdlib import PasswordHash
import jwt
# from datetime import datetime , timedelta

# Security Config
# pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


SECRET_KEY = 'analyse_comments'
ALGORITHM = 'HS256'
TOKEN_EXPIRES = 30

class Prediction(Base):
    __tablename__ = 'predictions'
    
    id = Column(Integer , primary_key=True)
    text = Column(String)
    predict_rate = Column(String)
    

class CreatePrediction(BaseModel):
    text:str


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer , primary_key = True)
    username = Column(String)
    password = Column(String , nullable=False)
    

class UserCreate(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    id:int
    username:str
    
class UserLogin(BaseModel):
    username:str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
# class TokenData(BaseModel):
#     username:str | None=None
    
# password_hash = PasswordHash.recommended()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')
    
    
# Security Functions

# def verify_pwd(plain_pws:str , hashed_pwd:str):
#     return pwd_context.verify(plain_pws , hashed_pwd)


# def get_pwd_hash(password:str):
#     return pwd_context.hash(password)

# def create_access_token(data:str):
#     to_encode = data.copy()
#     expire = datetime.utcnow()+ timedelta(minutes=15)
    
#     to_encode.update({"exp":expire})
#     encoded_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm =ALGORITHM)
    
#     return encoded_jwt

