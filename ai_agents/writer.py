# ai_agents/writer.py

import os
import google.generativeai as genai

# Load .env values
from dotenv import load_dotenv
load_dotenv()

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ai_writer_spin(text):
    print("\n>> Rewriting chapter using Gemini AI Writer...")
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            f"Rewrite this book chapter into a modern, clear, and engaging version:\n{text}",
        )
        return response.text.strip()
    except Exception as e:
        print("[Gemini Writer Error]", e)
        return "ERROR: Gemini Writer Failed"
