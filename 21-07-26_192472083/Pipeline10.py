from transformers import pipeline
sentiment = pipeline("sentiment-analysis")
result = sentiment("Python programming is easy and interesting.")
print(result)