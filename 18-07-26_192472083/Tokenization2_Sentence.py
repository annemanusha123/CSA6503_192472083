from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')
text = "Hello! Welcome to NLP. Python is easy to learn."
sentences = sent_tokenize(text)
print("Original Text:")
print(text)
print("\nSentence Tokens:")
for sentence in sentences:
    print(sentence)