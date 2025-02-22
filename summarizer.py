import google.generativeai as genai
import os
import pypdf

# Set your Google Gemini API key
GOOGLE_API_KEY = "AIzaSyAtrxCJY1lmfwkRoJ0_9dILdwQKXOs-RnE"
genai.configure(api_key=GOOGLE_API_KEY)

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = pypdf.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print("Error extracting text:", str(e))
    return text

def summarize_text(text):
    """Generates a summary using Google Gemini API."""
    model = genai.GenerativeModel("gemini-pro")
    
    try:
        response = model.generate_content(f"Summarize this legal document:\n{text}")
        return response.text if response else "⚠️ No summary generated."
    except Exception as e:
        return f"⚠️ Error in summarization: {str(e)}"
