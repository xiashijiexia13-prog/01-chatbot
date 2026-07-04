from app.prompt import SYSTEM_PROMPT
from app.chatbot import ask_ai
from app.history import save_history
from app.history import load_history
from app.logger import logger

logger.info("聊天机器人启动")

previous_history = load_history()

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

messages.extend(previous_history)

if previous_history:
    print("（之前的聊天记录已恢复）\n")

while True:
    question = input("你：")

    if question == "退出":
        print("聊天结束，再见！")
        break

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    answer = ask_ai(messages)

    print("\nAI：")
    print(answer)
    print("-" * 50)

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    save_history(messages)