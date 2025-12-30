from flask import Flask  #lightweight  Framework
import pandas as pd #dataframe work readinf csv rowcoulmb
import google.generativeai as genai 
from dotenv import load_dotenv
import os

#step call Api key model

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model= genai.GenerativeModel("gemini-2.5-flash")

df = pd.read_csv("qa_data (1).csv")

#csv into context text
context_text = ""
for _,row in df.iterrows():
    context_text +=  f"Q: {row['question']}\nA: {row['answer']}\n\n"

def ask_gemini(query):
    prompt = f"""
    You are Q&A assistant.

    Answer ONLY using the conteext below.
    If the answer is not present, say: No relevent Q&A found.

    context:
    {context_text}

    Question: {query}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

print("RAG Custome  Q&A Chatbot")
print("Enter exit come outside or terminate")


while True:
    user_input = input("You: ")
    if user_input.lower()=="exit":
        print("Good Bye")
        break

    answer=ask_gemini(user_input)          
    print(f"{answer}\n")
