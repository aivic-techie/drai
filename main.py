import os
import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")
chat_model = "gpt-3.5-turbo"

# Initialize FastAPI app
app = FastAPI()

# Define a class for the request body
class UserMessage(BaseModel):
    message: str

# Welcome message
print("Dr. AI: Welcome! I'm here to help you with your medical queries. Please describe your symptoms.")

# Initial system message
messages = [
    {"role": "system", "content": "You are a medical assistant. Respond in a friendly tone with concise answers. Ask relevant follow-up questions. In severe cases, advise the user to go to the hospital immediately."},
]

# POST endpoint to receive user messages
@app.post("/chat/")
async def chat(user_message: UserMessage):
    print({"reply": "Dr. AI: Goodbye! Stay healthy."})
    global messages
    message_content = user_message.message.strip().lower()

    # Handling special commands (exit, clear, help, info)
    if message_content == "exit":
        return {"reply": "Dr. AI: Goodbye! Stay healthy."}
    elif message_content == "clear":
        messages = [{"role": "system", "content": "You are a medical assistant capable of understanding symptoms."}]
        return {"reply": "Dr. AI: Conversation cleared. Please describe your symptoms."}
    elif message_content == "help":
        return {"reply": "Dr. AI: You can describe your symptoms or ask health-related questions. Type 'clear' to restart our conversation or 'exit' to end it."}
    elif message_content == "info":
        return {"reply": "Dr. AI: I'm an AI-powered assistant trained to provide preliminary medical advice. Remember to consult a healthcare professional for accurate diagnosis."}
    else:
        # Add the user message to the conversation history
        messages.append({"role": "user", "content": message_content})
        try:
            chat_completion = openai.ChatCompletion.create(model=chat_model, messages=messages)
            reply = chat_completion["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            return {"reply": reply}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# GET endpoint to retrieve conversation history
@app.get("/history/")
async def get_history():
    return {"messages": messages[1:]}
