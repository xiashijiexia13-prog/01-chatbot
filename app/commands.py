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

    if command == "/help":
        return None, (
            "支持的命令：\n"
            "/help   查看帮助\n"
            "/clear  清空聊天记录"
        )

    return None, "未知命令，输入 /help 查看帮助。"