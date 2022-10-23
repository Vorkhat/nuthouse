from fastapi import FastAPI, Depends
from telegram.schemas.messages import MessageBodyModel

telegram = FastAPI()


@telegram.post("/webhook")
async def callback(event: MessageBodyModel):
    print(event)

