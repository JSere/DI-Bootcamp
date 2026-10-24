import faiss
import numpy as np
import torch
from transformers import AutoModel, AutoTokenizer, pipeline

# 1. Knowledge source (sample documents)
documents = [
    (
        "Retrieval-Augmented Generation (RAG) combines external document"
        " retrieval with text generation."
    ),
    (
        "BERT is a transformer-based bidirectional model pretrained on a large"
        " text corpus."
    ),
    (
        "Vector databases like FAISS enable lightning-fast similarity search"
        " over dense vector embeddings."
    ),
]

# 2. Load pre-trained BERT model and tokenizer for embeddings
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


def get_bert_embedding(text: str) -> np.ndarray:
  """Generates a dense vector embedding for a given text using BERT mean pooling."""
  inputs = tokenizer(
      text, return_tensors="pt", padding=True, truncation=True, max_length=512
  )
  with torch.no_grad():
    outputs = model(**inputs)
  # Mean pooling over the token sequence to get a single vector per document
  embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
  return embedding


# Generate embeddings for all documents in the knowledge base
doc_embeddings = np.array([get_bert_embedding(doc) for doc in documents])

# 3. Store document embeddings in a FAISS vector index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)


# 4. Retriever implementation
def retrieve_documents(query: str, k: int = 2) -> list[str]:
  """Retrieves the top-k most relevant documents for a given query vector."""
  query_emb = np.array([get_bert_embedding(query)])
  distances, indices = index.search(query_emb, k)
  return [documents[i] for i in indices[0]]


# 5. Initialize generator model (Flan-T5 for question answering)
generator = pipeline("text2text-generation", model="google/flan-t5-small")


# 6. Complete RAG Pipeline execution
def answer_question(query: str) -> str:
  """RAG pipeline: retrieves relevant context and generates an answer using LLM."""
  retrieved_docs = retrieve_documents(query, k=2)
  context = " ".join(retrieved_docs)
  prompt = (
      f"Context: {context}\n\nQuestion: {query}\n\nAnswer based on context:"
  )
  response = generator(prompt, max_length=128)[0]["generated_text"]
  return response


# 7. Main execution test
if __name__ == "__main__":
  sample_query = "What does RAG combine?"
  print(f"Query: {sample_query}")
  print(f"Retrieved Documents: {retrieve_documents(sample_query, k=2)}")
  print(f"Generated Answer: {answer_question(sample_query)}")