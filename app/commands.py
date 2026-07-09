from app.prompt import SYSTEM_PROMPT

def clear_messages():

    return {
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ],
        "message": "聊天记录已清空！"
    }


def is_command(text):
    return text.startswith("/")

def execute_command(command):

    if command not in COMMANDS:
        return None, "未知命令，输入 /help 查看帮助。"

    result = COMMANDS[command]()

    return result["messages"], result["message"]

def help_message():

    return {
        "messages": None,
        "message": (
            "支持的命令：\n"
            "/help   查看帮助\n"
            "/clear  清空聊天记录"
        )
    }

COMMANDS = {
    "/clear": clear_messages,
    "/help": help_message
}