from typing import Union

from fastapi import FastAPI

# from feat/comfy_client/client.py
from feat.comfy_client.client import ComfyClient

# from "feat/comfy_client/client.py" import ComfyClient

app = FastAPI()


@app.get("/")
def read_root():
    ComfyClient.queue_prompt("masterpiece")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
