from fastapi import FastAPI
from config import Config
from telegram.schemas.messages import MessageBodyModel, Chat

telegram = FastAPI()


def decode_event(event) -> MessageBodyModel:
    """
        during local development, there was a problem with the encoding of some fields
        message=Message(message_id=169, from_field=None, sender_chat=None, date=1666442493, chat=Chat(id=1311888287, type='private', title=None, username='Traikan', first_name='Р•РІРіРµРЅРёР№', last_name='Р”РѕСЂРѕС„РµРµРІ', photo=None, bio=None, has_private_forwards=None))
    """

    key: Chat = event.message.chat

    def encode(string):

        print(string.encode('cp1251').decode('utf-8'))

    key.first_name = encode(key.first_name)
    key.last_name = encode(key.last_name)

    return event


@telegram.post("/webhook")
async def callback(event: MessageBodyModel):
    if Config.Debug:
        ...
    else:
        event = decode_event(event)
        print(event)
