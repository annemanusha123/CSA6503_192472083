from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
text = "Artificial Intelligence is amazing."
tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)
ids = tokenizer.convert_tokens_to_ids(tokens)
print("Token IDs:", ids)