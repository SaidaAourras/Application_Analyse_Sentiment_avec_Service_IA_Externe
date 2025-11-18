import os
# from huggingface_hub import InferenceClient
import requests
from dotenv import load_dotenv

load_dotenv()

# client = InferenceClient(
#     provider="hf-inference",
#     api_key=os.getenv("HF_TOKEN"),
# )

# result = client.text_classification(
#     "I like you. I love you",
#     model="nlptown/bert-base-multilingual-uncased-sentiment",
# )

# print(result)


def hugging_face_nlp(comment):
    API_URL = "https://router.huggingface.co/hf-inference/models/nlptown/bert-base-multilingual-uncased-sentiment"
    headers = {
        "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": comment,
    })

    return output