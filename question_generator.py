import requests

def generate_questions_with_tinyllama(chunks):
	prompt = (
		"Given the following resume information, generate 5 interview questions:\n\n" + "\n".join(chunks)
	)
	response = requests.post(
		"http://localhost:11434/api/generate",
		json={"model": "tinyllama", "prompt": prompt, "stream": False}
	)
	try:
		result = response.json()
	except Exception as e:
		print("Response text:", response.text)
		raise e
	return [q for q in result['response'].split('\n') if q.strip()]