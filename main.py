from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from PIL import Image

import json
import io
from datetime import datetime

# Create the FastAPI app
app = FastAPI()


@app.get('/')
def read_root():
    return {"Hello": ["Minjoon", "Hyunseo"]}

@app.get("/items/")
def read_item(q: Optional[str] = None):
    results = {"items": [{"item_id": "Minjoon"}, {"item_id": "Heyonseo"}]}
    if q:
        results.update({"q": q})
    return results

@app.post("/items/")
def read_item(q: str):
    results = ""
    if q == "가위" :
        results = "나는 묵인데 너가 졌네 ㅎㅎ"
    elif q == "바위" :
        results = "나는 빠인데 너가 졌네 ㅎㅎ"
    elif q == "보" :
        results = "나는 찌인데 너가 졌네 ㅎㅎ"
    else : 
        results = "가위바위보만 내라구~"

    return results

class UserPydantic(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user_pydantic = UserPydantic(**external_data)