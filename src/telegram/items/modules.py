from httpx import AsyncClient
from config import Config


async def set_webhook(host_url) -> bool:
    async with AsyncClient() as client:
        payload = {"url": f"{host_url}/webhook"}
        request = await client.post(Config.TELEGRAM_SET_WEBHOOK_URL, json=payload)
        print(request.json())
        return request.status_code == 200
