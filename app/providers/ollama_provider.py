from ollama import chat

from app.config import MODEL_NAME


def chat_with_ollama(messages):
    response = chat(
        model=MODEL_NAME,
        messages=messages
    )

    return response["message"]["content"]