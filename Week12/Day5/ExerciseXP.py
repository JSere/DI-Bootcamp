from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sentence = "Learning how BERT tokenizes text is very exciting!"

tokens = tokenizer.tokenize(sentence)
print("Individual tokens:", tokens)

inputs = tokenizer(
    sentence, 
    return_tensors="pt", 
    padding=True, 
    truncation=True, 
    max_length=128
)

print("\nInput IDs tensor:", inputs['input_ids'])
print("Decoded tokens:", tokenizer.convert_ids_to_tokens(inputs['input_ids'][0]))