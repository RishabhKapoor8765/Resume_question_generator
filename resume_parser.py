import PyPDF2
from PyPDF2.errors import PdfReadError

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    except PdfReadError:
        return "Error: The uploaded file is not a valid PDF."