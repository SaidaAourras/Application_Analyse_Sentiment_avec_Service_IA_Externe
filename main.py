from database import Base , engine
from fastapi import FastAPI , Depends , HTTPException , status
from sqlalchemy.orm import Session
from database import session_m
from models import User , UserCreate , Prediction , UserLogin , UserComment
from auth import verify_token , create_token
from Inference_providers import hugging_face_nlp
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()

# ------------- cors config ----------------------

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def get_db():
    session = session_m()
    try:
        yield session
    finally:
        session.close()
        
# test

@app.get('/')
def hello():
     return 'hello world'
# my endpoints
@app.post('/sentiment')
def predict(dataComment:UserComment , db:Session=Depends(get_db) , payload=Depends(verify_token)):
     user = db.query(User).filter(User.username == payload['sub']).first()
     if not user:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                              detail='Could not validate user')
          
     comment = dataComment.comment
     results = hugging_face_nlp(comment)
     # print(type(result))
     labels = []
     scores = []
     
     print(results)
     for result in results[0]:
          labels.append(result['label'])
          scores.append(result['score'])
     
     nb_star = labels[scores.index(max(scores))]
     
     new_prediction = Prediction(
          text = comment,
          predict_rate = nb_star.split(' ')[0]
     )
     
     db.add(new_prediction)
     db.commit()
     db.refresh(new_prediction)
     
     return new_prediction

@app.post('/register')
def create_user(user:UserCreate , db:Session=Depends(get_db) ):
     new_user = User(
          username = user.username,
          password = user.password
     )
     
     db.add(new_user)
     db.commit()
     db.refresh(new_user)
     
     return new_user



@app.post('/login')
def login(user:UserLogin ,db:Session=Depends(get_db) ):
     user = db.query(User).filter(User.username == user.username).first()
     
     if not user:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                              detail='Could not validate user')
     
     token = create_token(user.username , user.id)
     
     return {'access_token': token , 'token_type':'bearer'}
     


