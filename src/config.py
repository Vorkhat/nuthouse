from tokens import Tokens
from dotenv import load_dotenv

load_dotenv()


class Config:

    Debug = False
    DEBUG_SERVER = ''

    REPOSITORY = 'nuthouse'
    HOST_URL = "http://94.103.93.53"
    PORT_APP = 80
    PORT_CI_CD = 8080

    SQLALCHEMY_POSTGRESQL_URL = f'postgresql+asyncpg://{Tokens.POSTGRESQL_USER}:{Tokens.POSTGRESQL_PASSWORD}@localhost/{Tokens.POSTGRESQL_DATABASE}'

    TELEGRAM_SET_WEBHOOK_URL = f"https://api.telegram.org/bot{Tokens.TELEGRAM_TOKEN}/setWebhook"
