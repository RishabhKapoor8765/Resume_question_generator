import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()
collection = client.get_or_create_collection(name="resumes")

def create_vector_store(text):
	# Split text into chunks of 500 characters
	chunks = [text[i:i+500] for i in range(0, len(text), 500)]
	embed_fn = embedding_functions.DefaultEmbeddingFunction()
	embeddings = [embed_fn(chunk) for chunk in chunks]
	# Convert embeddings to list format
	embeddings = [embedding[0].tolist() if hasattr(embedding[0], 'tolist') else list(embedding[0]) for embedding in embeddings]
	ids = [str(i) for i in range(len(chunks))]
	collection.add(documents=chunks, embeddings=embeddings, ids=ids)

def query_vector_store(query, top_k=5):
	embed_fn = embedding_functions.DefaultEmbeddingFunction()
	query_emb = embed_fn(query)
	query_emb = [query_emb[0].tolist() if hasattr(query_emb[0], 'tolist') else list(query_emb[0])]
	results = collection.query(query_embeddings=query_emb, n_results=top_k)
	return results["documents"][0]