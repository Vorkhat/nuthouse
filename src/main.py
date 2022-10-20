from fastapi import FastAPI
from routing import create_routing

app = FastAPI()

create_routing(app)

