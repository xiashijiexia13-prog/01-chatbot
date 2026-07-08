from app.config import AI_PROVIDER
from app.logger import logger
from app.providers.ollama_provider import chat_with_ollama

def ask_ai(messages):
    try:
        if AI_PROVIDER == "ollama":
            return chat_with_ollama(messages)
        else:
            return "暂不支持该AI服务"

    except Exception as e:
        logger.error(f"AI调用失败：{e}")
        return "AI 当前不可用，请稍后再试。"