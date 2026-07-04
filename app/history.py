import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_FILE = os.path.join(BASE_DIR, "data", "history.json")


def save_history(messages):
    """保存对话历史（仅保存 user 和 assistant 消息，不保存 system 提示）"""
    # 过滤掉 system 消息，只保存用户和助手的对话
    chat_history = [m for m in messages if m["role"] in ("user", "assistant")]

    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            chat_history,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_history():
    """加载对话历史，返回 user/assistant 消息列表"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            try:
                history = json.load(file)
                print(f"已加载 {len(history)} 条聊天记录")
                return history
            except json.JSONDecodeError:
                print("聊天记录文件损坏，将重新开始")
                return []
    else:
        print("没有找到聊天记录，开始新对话")
        return []