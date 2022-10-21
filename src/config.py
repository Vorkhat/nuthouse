from src.tokens import Tokens
from dotenv import load_dotenv

load_dotenv()


class Config:
    REPOSITORY = 'nuthouse'
    HOST_URL = "94.103.93.53"
    PORT_APP = 80
    PORT_CI_CD = 8080

    TELEGRAM_SET_WEBHOOK_URL = f"https://api.telegram.org/bot{Tokens.TELEGRAM_TOKEN}/setWebhook"
