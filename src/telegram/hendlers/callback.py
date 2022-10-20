from fastapi import FastAPI

telegram = FastAPI()


@telegram.post("/webhook")
async def callback():
    pass
