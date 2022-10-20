from fastapi import FastAPI
from telegram.hendlers.callback import telegram


def create_routing(app: FastAPI):
    app.include_router(telegram.router)
