from ollama import chat
from app.config import MODEL_NAME
from app.logger import logger


def ask_ai(messages):
    try:
        response = chat(
            model=MODEL_NAME,
            messages=messages
        )
        return response["message"]["content"]

    except Exception as e:
        logger.error(f"AI调用失败：{e}")
        return "AI 当前不可用，请稍后再试。"