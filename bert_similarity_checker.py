from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F

# Load pre-trained BERT model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_bert_embeddings(code_snippet):
    inputs = tokenizer(code_snippet, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def bert_similarity_checker(code1, code2):
    emb1 = get_bert_embeddings(code1)
    emb2 = get_bert_embeddings(code2)
    
    similarity = F.cosine_similarity(emb1, emb2)
    return similarity.item()
