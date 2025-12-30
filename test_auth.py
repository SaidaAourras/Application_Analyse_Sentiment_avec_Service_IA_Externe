from fastapi import FastAPI , Depends 
from fastapi.security import APIKeyHeader
from jose import jwt 
# from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

api_key_header = APIKeyHeader(name="Authorization")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# FAKE_JWT = "TOKEN123"

SECRET_KEY = 'JHFHNAW89U89iounep948tnpejgvyB&*7wrnwe9839rjdfmkauep9trm'
ALGO = "HS256"

# avec python-jose on cree le token
def create_token(username:str):
    payload = {
        'sub': username
    }
    return jwt.encode(payload , SECRET_KEY , algorithm=ALGO)

@app.post("/login")
def login(username: str, password: str):
    if username == "alice" and password == "secret":
        token = create_token(username)
        print(token)
    return {"acces_token": token}



def verify_token(api_key: str = Depends(api_key_header)):
    payload = jwt.decode(api_key , SECRET_KEY , algorithms=ALGO)
    
    print(payload)
    return payload


@app.get("/secret")
def secret(token = Depends(verify_token)):
    return {"data": "TOP SECRET"}