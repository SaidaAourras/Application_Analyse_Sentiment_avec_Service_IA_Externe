from database import Base , engine
from fastapi import FastAPI
from Inference_providers import hugging_face_nlp


app = FastAPI()

Base.metadata.create_all(engine)

@app.post('/predict')
def predict(comment:str):
     results = hugging_face_nlp(comment)
     # print(type(result))
     labels = []
     scores = []
     
     print(results)
     for result in results[0]:
          labels.append(result['label'])
          scores.append(result['score'])
     
     nb_star = labels[scores.index(max(scores))]
          
     return nb_star


