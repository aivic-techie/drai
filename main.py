import os
import openai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")
chat_model = "gpt-3.5-turbo"

# Initialize FastAPI app
app = FastAPI()

origins = [
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define a class for the request body
class UserMessage(BaseModel):
    message: str


# Initial system message
messages = [
    {
        "role": "system",
        "content": "As a medical assistant, provide clear and concise medical guidance and diagnosis. Communicate reassuringly and engage with users by asking pertinent follow-up questions to help with the diagnosis and guidance. Direct users to professional medical help for serious health concerns."
    }
]

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to Drai API!"}


# POST endpoint to receive user messages
@app.post("/chat/")
async def chat(user_message: UserMessage):
    global messages
    message_content = user_message.message.strip().lower()

    # Handling special commands (exit, clear, help, info)
    if message_content == "/exit":
        return {"reply": "Dr. Anne: Goodbye! Stay healthy."}
    elif message_content == "/clear":
        messages = [{"role": "system", "content": "You are a medical assistant capable of understanding symptoms."}]
        return {"reply": "Dr. Anne: Conversation cleared. Please describe your symptoms."}
    elif message_content == "/help":
        return {"reply": "Dr. Anne: You can describe your symptoms or ask health-related questions. Type 'clear' to restart our conversation or 'exit' to end it."}
    elif message_content == "/info":
        return {"reply": "Dr. Anne: I'm an AI-powered assistant trained to provide preliminary medical advice. Remember to consult a healthcare professional for accurate diagnosis."}
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
    pass
    return {"messages": messages[1:]}
