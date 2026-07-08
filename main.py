from app.prompt import SYSTEM_PROMPT
from app.chatbot import ask_ai
from app.history import save_history
from app.history import load_history
from app.logger import logger
from app.config import MAX_HISTORY
from app.commands import is_command, execute_command

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

    if is_command(question):

        new_messages, result = execute_command(question)

        if new_messages is not None:
            messages = new_messages
            save_history(messages)

        if result:
            print(result)

            continue

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

    system_message = messages[0]

    history = messages[1:]

    history = history[-MAX_HISTORY:]

    messages = [system_message] + history

    save_history(messages)