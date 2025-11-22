from fastapi import HTTPException , status , Depends
from fastapi.security import APIKeyHeader
from jose import jwt , JWTError
from dotenv import load_dotenv
import os

load_dotenv()

api_key_header = APIKeyHeader(name="Authorization")


SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

def create_token(username:str, user_id:str):
    encode = {'sub':username , 'id':user_id}
    return jwt.encode(encode , SECRET_KEY , algorithm=ALGORITHM)


def verify_token(token:str=Depends(api_key_header)):
    try:
            if token.startswith("Bearer "):
                token = token.split(" ")[1]
            payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
            return payload
    except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='token invalide',
                headers={"WWW-Authenticate": "Bearer"}
            )