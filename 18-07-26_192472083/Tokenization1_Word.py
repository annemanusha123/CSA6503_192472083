from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
text = "Natural Language Processing is interesting."
tokens = word_tokenize(text)
print("Original Text:")
print(text)
print("\nWord Tokens:")
print(tokens)