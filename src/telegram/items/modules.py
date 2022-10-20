from httpx import AsyncClient
from src.config import Config


async def set_webhook() -> bool:
    async with AsyncClient() as client:
        payload = {"url": f"{Config.HOST_URL}/webhook"}
        request = await client.post(Config.TELEGRAM_SET_WEBHOOK_URL, json=payload)
        return request.status_code == 200
