import google.generativeai as genai
import PyPDF2
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Error: File '{pdf_path}' not found. Ensure the file is uploaded correctly.")

    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    
    return text.strip() if text.strip() else "No readable text found in the document."

# Function to summarize text using Gemini API
def summarize_text(text):
    if not text.strip():
        return "No valid text to summarize."

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize this legal document:\n{text}")
    return response.text if response else "Summarization failed."

# Example usage
if __name__ == "__main__":
    pdf_path = os.path.join(os.getcwd(), "uploaded.pdf")  # Absolute path for reliability
    
    try:
        if os.path.exists(pdf_path):
            print(f"Processing file: {pdf_path}")
        else:
            print(f"File '{pdf_path}' not found. Ensure it is uploaded via Streamlit.")
        
        text = extract_text_from_pdf(pdf_path)
        print("\nExtracted Text:\n", text[:1000])  # Print first 1000 characters for debugging
        
        summary = summarize_text(text)
        print("\nGenerated Summary:\n", summary)
    except Exception as e:
        print(f"Error: {e}")
