🤖 AI Resume Chatbot
A Streamlit-based AI chatbot that generates interview questions from uploaded resumes using local LLMs like TinyLlama. The project combines PDF parsing, semantic embedding, and vector search with ChromaDB to deliver context-aware question generation.

🚀 Features
- 📄 Upload resumes in PDF format via a Streamlit UI
- 🧠 Parse and extract resume content automatically
- 🔍 Generate embeddings 
- 🗃️ Store and retrieve data using ChromaDB
- 🤖 Generate interview questions using TinyLlama or any compatible local model via Ollama
- 🔄 Easily switch models based on system resources or preference

🛠️ Tech Stack
| Streamlit | Interactive UI for uploading and chatting | 
| TinyLlama | Lightweight local LLM for question generation | 
| Ollama | Local model server for LLM inference | 
| ChromaDB | Embedding storage and semantic search | 
| PyPDF2 | PDF parsing and text extraction | 



📦 Installation
git clone https://github.com/yourusername/chatbot_ai.git
cd chatbot_ai
>>>Install the other libraries required


Make sure Ollama is installed and running:
ollama serve
ollama pull tinyllama



🧪 Usage
- Run the Streamlit app:
streamlit run app.py
- Upload a resume in PDF format.
- The app will parse the resume, create embeddings, and store them in ChromaDB.
- The selected model will generate interview questions based on the resume content.

🔄 Model Flexibility
You can replace tinyllama with any other model supported by Ollama (e.g., llama2, mistral, gemma) depending on your system's memory and performance.


🙌 Contributing
Pull requests are welcome! If you’d like to add new features, improve performance, or support more models, feel free to fork and submit a PR.

📄 License
This project is open-source under the MIT License.

Let me know if you want to add badges, screenshots, or deployment instructions — I can help polish it even further.
