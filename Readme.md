# Drai Medical Chatbot

Welcome to the Drai Medical Chatbot! This application leverages the OpenAI GPT-3.5 Turbo model that has been fine-tuned to simulate a medical assistant capable of providing preliminary medical advice. Users can interact with the chatbot by sending messages describing their symptoms or asking health-related questions.

## Getting Started

To get started with the chatbot, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/aivic-techie/drai.git
    cd drai
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:

    Create a `.env` file in the project root and add your OpenAI API key:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

4. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

    The application will be accessible at `http://127.0.0.1:8000`.


## Usage

### Swager UI

Swagger UI provides a convenient way to test your API endpoints. Visit http://127.0.0.1:8000/docs in your browser to explore and interact with the API.

### Chat Endpoint

Send a POST request to /chat/ with a JSON payload containing the user's message. The Swagger UI allows you to input and test different requests.

OR

Send a POST request to `/chat/` with a JSON payload containing the user's message:

```bash
curl -X POST "http://127.0.0.1:8000/chat/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"message": "I have a headache"}'
```
### Special Commands

The chatbot recognizes special commands such as exit, clear, help, and info. Use these commands to interact with the chatbot:

exit: End the conversation.

clear: Clear the conversation history and start a new session.

help: Get information on using the chatbot.

info: Learn more about the chatbot and its capabilities.

### Conversation History

To retrieve the conversation history, send a GET request to /history/ using the Swagger UI 

OR

```bash
curl -X GET "http://127.0.0.1:8000/history/" -H "accept: application/json"
```

### Test

To run the tests in the script

```bash
pytest test_main.py
```
### Feedback

Your feedback is valuable! Feel free to provide input on the chatbot responses to help improve its performance.

### Acknowledgments

This project utilizes the OpenAI GPT-3.5 Turbo model for natural language processing.

Happy chatting with DRAI!




