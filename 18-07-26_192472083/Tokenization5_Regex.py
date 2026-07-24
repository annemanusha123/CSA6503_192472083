from nltk.tokenize import RegexpTokenizer
text = "Hello! NLP, Python 3.14 is awesome."
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)
print("Original Text:")
print(text)
print("\nRegex Tokens:")
print(tokens)