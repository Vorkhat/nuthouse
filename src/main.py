import asyncio
import uvicorn
import threading
import nest_asyncio
from config import Config
from fastapi import FastAPI
from telegram.items.modules import set_webhook
from pyngrok import ngrok
from routing import create_routing

app = FastAPI()

create_routing(app)


if __name__ == "__main__":

    if Config.Debug:
        threading.Thread(target=asyncio.run,  args=(set_webhook(Config.HOST_URL),), daemon=True).start()
        uvicorn.run(app, host="0.0.0.0", port=Config.PORT_APP)
    else:
        #https://github.com/inconshreveable/ngrok/issues/826
        #https://stackoverflow.com/questions/66615463/how-to-get-ngrok-https-url-with-pyngrok-in-python

        ngrok_tunnel = ngrok.connect(Config.PORT_APP, bind_tls=True)
        Config.DEBUG_SERVER = ngrok_tunnel.public_url

        threading.Thread(target=asyncio.run,  args=(set_webhook(Config.DEBUG_SERVER),), daemon=True).start()

        print(ngrok_tunnel)

        nest_asyncio.apply()
        uvicorn.run(app, host="0.0.0.0", port=Config.PORT_APP)
