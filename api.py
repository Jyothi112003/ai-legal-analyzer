import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("✅ API key is loaded correctly.")
else:
    print("❌ API key is missing. Check your .env file!")
