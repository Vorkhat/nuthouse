import os
import uvicorn
from fastapi import FastAPI
from src.config import Config

app = FastAPI()


@app.post("/")
def callback():
    os.system(f"cd {Config.REPOSITORY} && git pull && docker-compose up -d --build")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=Config.PORT_CI_CD)