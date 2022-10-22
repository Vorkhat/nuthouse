import os
from dotenv import load_dotenv

load_dotenv()


class Tokens:
    POSTGRESQL_USER = os.getenv('POSTGRESQL_USER')
    POSTGRESQL_PASSWORD = os.getenv('POSTGRESQL_PASSWORD')
    POSTGRESQL_DATABASE = os.getenv('POSTGRESQL_DATABASE')

    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

