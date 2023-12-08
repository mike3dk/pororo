from fastapi import Request, FastAPI
import json
from pororo.pororo import Pororo

app = FastAPI()
ner = Pororo(task="ner", lang="ko")


@app.get("/")
async def root():
    return {"message": "pororo"}


@app.post("/named_entity_recognition")
async def named_entity_recognition(request: Request):
    text = await request.json()
    out = ner(text["text"])
    return out
