# import os
# import openai
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Access the API key
# openai_api_key = os.getenv("OPENAI_API_KEY")
# fine_tuned_model = "davinci:ft-personal-2023-11-22-18-09-18"

# print("Dr. AI: Welcome! I'm here to help you with your medical queries. Please describe your symptoms.")

# conversation_history = '''You are a medical doctor assistant. Respond in a friendly and helpful tone, with very
# concise answers. Make sure to ask the user relevant follow up questions where necessary.\n'''

# while True:
#     user_input = input("👤: ").strip()

#     if user_input.lower() == "exit":
#         print("Dr. AI: Goodbye! Stay healthy.")
#         break
#     elif user_input.lower() == "clear":
#         print("\033[H\033[J")
#         conversation_history = "Dr. AI is a knowledgeable medical assistant. It can understand and respond to medical symptoms described by users.\n"
#         continue
#     elif user_input.lower() == "help":
#         print("Dr. AI: You can describe your symptoms or ask health-related questions. Type 'clear' to restart our conversation or 'exit' to end it.")
#         continue
#     elif user_input.lower() == "info":
#         print("Dr. AI: I'm an AI-powered assistant trained to provide preliminary medical advice. Remember to consult a healthcare professional for accurate diagnosis.")
#         continue

#     conversation_history += f"👤: {user_input}\n"
#     try:
#         response = openai.Completion.create(
#             model=fine_tuned_model,
#             prompt=conversation_history,
#             max_tokens=150,
#             stop=["\n", "👤:", "Dr. AI:"]
#         )
#         reply = response.choices[0].text.strip()
#         print(f"🤖: {reply}")
#         conversation_history += f"Dr. AI: {reply}\n"
#     except Exception as e:
#         print(f"Error: {e}")


import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai_api_key = os.getenv("OPENAI_API_KEY")
fine_tuned_model = "davinci:ft-personal-2023-11-22-18-09-18"

print("Dr. AI: Welcome! I'm here to help you with your medical queries. Please describe your symptoms.")

conversation_history = '''You are a medical doctor assistant. Respond in a friendly and helpful tone, with very
concise answers. Make sure to ask the user relevant follow up questions where necessary. If a user greets, respond to the greeting\n'''

while True:
    user_input = input("👤: ").strip()

    if user_input.lower() == "exit":
        print("Dr. AI: Goodbye! Stay healthy.")
        break
    elif user_input.lower() == "clear":
        print("\033[H\033[J")  # Clear the console
        conversation_history = "Dr. AI is a knowledgeable medical assistant. It can understand and respond to medical symptoms described by users.\n"
        continue
    elif user_input.lower() == "help":
        print("Dr. AI: You can describe your symptoms or ask health-related questions. Type 'clear' to restart our conversation or 'exit' to end it.")
        continue
    elif user_input.lower() == "info":
        print("Dr. AI: I'm an AI-powered assistant trained to provide preliminary medical advice. Remember to consult a healthcare professional for accurate diagnosis.")
        continue

    conversation_history += f"👤: {user_input}\n"
    try:
        response = openai.Completion.create(
            model=fine_tuned_model,
            prompt=conversation_history,
            max_tokens=150,
            stop=["\n", "👤:", "Dr. AI:"]
        )
        reply = response.choices[0].text.strip()

        if reply:  # Check if the reply is not empty
            print(f"🤖: {reply}")
            conversation_history += f"Dr. AI: {reply}\n"
        else:
            print("🤖: I'm here to provide medical assitance. Could you please provide more details?")
            conversation_history += '''Dr. AI: I'm not sure how to respond to that. Could you please provide more details?\nI'm here to help you with your medical queries. Please describe your symptoms.'''

    except Exception as e:
        print(f"Error: {e}")
