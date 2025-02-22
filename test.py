import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ API key is missing! Check your .env file.")

client = openai.OpenAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print("✅ OpenAI API is working! Response:", response.choices[0].message.content)
except openai.OpenAIError as e:
    print("❌ OpenAI API Error:", e)
