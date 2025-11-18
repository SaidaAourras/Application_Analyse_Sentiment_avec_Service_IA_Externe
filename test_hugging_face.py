from transformers import pipeline

model = pipeline("sentiment-analysis" , model="nlptown/bert-base-multilingual-uncased-sentiment")

response = model("text to analyse")

print(response)