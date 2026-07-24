from transformers import BertTokenizer, BertModel
import torch
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
sentences = [
    "The cat is sitting on the mat.",
    "A cat is resting on the mat."
]
for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    print(sentence)
    print(outputs.last_hidden_state.shape)