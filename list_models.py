import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit()

genai.configure(api_key=API_KEY)

print("Daftar Model Gemini yang Tersedia:")
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(f"- {m.name} (Didukung untuk generateContent)")
    else:
        print(f"- {m.name} (TIDAK didukung untuk generateContent)")
