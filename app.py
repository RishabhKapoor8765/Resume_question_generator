import streamlit as st
import os
from resume_parser import extract_text_from_pdf
from vector_store import create_vector_store, query_vector_store
from question_generator import generate_questions_with_tinyllama

st.title("Resume Interview Question Generator")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
	os.makedirs("sample_resumes", exist_ok=True)
	file_path = os.path.join("sample_resumes", uploaded_file.name)
	with open(file_path, "wb") as f:
		f.write(uploaded_file.getbuffer())
	st.success("Resume uploaded successfully!")
	text = extract_text_from_pdf(file_path)
	create_vector_store(text)  # Store embeddings in ChromaDB

	if st.button("Generate Interview Questions"):
		# Retrieve relevant chunks (for demo, we use all text)
		relevant_chunks = query_vector_store("interview questions", top_k=5)
		print(relevant_chunks)
		# Generate questions using tinyllama via Ollama
		questions = generate_questions_with_tinyllama(relevant_chunks)
		st.markdown("### Suggested Questions:")
		for q in questions:
			st.write(q)