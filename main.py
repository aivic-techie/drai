import os
import openai
from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware as CORSMiddleware  # noqa
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")
chat_model = "gpt-3.5-turbo"
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
]

app = FastAPI(title="Drai")

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows only specific origins
    # allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["POST", "GET"],  # Allows methods
    allow_headers=["*"],  # Allows all headers
    expose_headers=["*"],
)


# Initialize FastAPI app
# app = FastAPI(title="Drai", middleware=middleware)

# Define a class for the request body
class UserMessage(BaseModel):
    message: str


# Initial system message
messages = [
    {
        "role": "system",
        "content": '''As Dr. Anne, offer clear and concise medical guidance and medical diagnosis. Don't start with "I'm not a doctor", there are disclaimers already in the platform you're being deployed. Engage users reassuringly and ask pertinent follow-up questions to aid in diagnosis. If serious health concerns arise, promptly direct users to seek professional medical help.'''
    }
]

@app.get("/")
async def root():
    pass
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
    chat_history = messages[1:]
    if not chat_history:
        chat_history = "Drai"
    return {"messages": chat_history}
