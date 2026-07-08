from app.prompt import SYSTEM_PROMPT

def clear_messages():   
    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


def is_command(text):
    return text.startswith("/")

def execute_command(command):

    if command == "/clear":
        return clear_messages(), "聊天记录已清空！"

    return None, None