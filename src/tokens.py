import os
from dotenv import load_dotenv

load_dotenv()


class Tokens:
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

