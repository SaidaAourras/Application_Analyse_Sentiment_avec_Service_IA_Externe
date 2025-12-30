from datetime import timedelta , datetime
from models import User
from fastapi.security import OAuth2PasswordBearer 
from fastapi import Depends , HTTPException , status
from jose import jwt , JWTError
from typing import Annotated



SECRET_KEY = "ksdjhf8r98wejkrjweriu8w3uresfjhwn8re789w3jshfdjskhfiq37498023@$#^$W6786e8wrneVTR376t495wyrenio0r9"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')

def verify_token(token:str=Depends(oauth2_scheme)):
     try:
          payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
          return payload
     except JWTError:
          raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail='token invalide',
               headers={"WWW-Authenticate": "Bearer"}
          )

def authenticated_user(username:str , password:str , db):
     user = db.query(User).filter(User.username == username).first()
     if not user:
          return False
     return user

def create_access_token(username:str , user_id:int , expires_delta:timedelta):
     encode = {'sub':username , 'id':user_id}
     expires = datetime.utcnow() + expires_delta
     encode.update({'exp':expires})
     return jwt.encode(encode , SECRET_KEY , algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str ,Depends(oauth2_scheme)]):
     try:
          payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
          username : str = payload.get('sub')
          user_id: int = payload.get('id')
          if username is None or user_id is None:
               raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                   detail='Could not validate user')
          return {'username':username , 'id':user_id}
     except JWTError:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                   detail='Could not validate user')


