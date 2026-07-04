from ollama import chat
from app.config import MODEL_NAME

def ask_ai(messages):
    try:
        response = chat(
            model=MODEL_NAME,
            messages=messages
        )
        return response["message"]["content"]

    except Exception as e:
        return f"发生错误：{e}"