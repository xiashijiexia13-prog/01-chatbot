from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

SYSTEM_NAME = os.getenv("SYSTEM_NAME")

MAX_HISTORY = int(os.getenv("MAX_HISTORY"))

AI_PROVIDER = os.getenv("AI_PROVIDER")
