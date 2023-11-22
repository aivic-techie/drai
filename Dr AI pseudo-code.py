import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai_api_key = os.getenv("OPENAI_API_KEY")
chat_model = "gpt-3.5-turbo"

print("Dr. AI: Welcome! I'm here to help you with your medical queries. Please describe your symptoms.")

messages = [
    {"role": "system", "content": '''You are a medical assistant capable of understanding symptoms. Respond in a friendly and helpful tone, with very
concise answers. Make sure to ask the user relevant follow up questions. Also, if the case is severe, tell user to go immediately to hospital'''},
]

# Initial chatbot setup
try:
    chat_completion = openai.ChatCompletion.create(model=chat_model, messages=messages)
    reply = chat_completion["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
except Exception as e:
    print(f"Error: {e}")
    exit()

while True:
    message = input("👤: ").strip().lower()
    if message == "exit":
        print("Dr. AI: Goodbye! Stay healthy.")
        break
    if message == "clear":
        print("\033[H\033[J")
        print("Dr. AI: I'm here to help you with your medical queries. Please describe your symptoms.")
        messages = [{"role": "system", "content": "You are a medical assistant capable of understanding symptoms."}]
        continue
    if message == "help":
        print("Dr. AI: You can describe your symptoms or ask health-related questions. Type 'clear' to restart our conversation or 'exit' to end it.")
        continue
    if message == "info":
        print("Dr. AI: I'm an AI-powered assistant trained to provide preliminary medical advice. Remember to consult a healthcare professional for accurate diagnosis.")
        continue

    if message:
        messages.append({"role": "user", "content": message})
        try:
            chat_completion = openai.ChatCompletion.create(model=chat_model, messages=messages)
            reply = chat_completion["choices"][0]["message"]["content"]
            print(f"🤖: {reply}")
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"Error: {e}")

    # # Optional: Implement a feedback mechanism
    # feedback = input("👤: Was this advice helpful? (yes/no) ").strip().lower()
    # if feedback == "yes":
    #     print("Dr. AI: Great to hear that! Do you have any other questions?")
    # elif feedback == "no":
    #     print("Dr. AI: Sorry to hear that. I'll try to improve. Please consult a healthcare professional for more accurate advice.")
