import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_answer(question, context):
    prompt = f"""You are an assistant that answers questions based on image context.
Context: {context}
Question: {question}
Answer:"""
    response = model.generate_content(prompt)
    return response.text.strip()