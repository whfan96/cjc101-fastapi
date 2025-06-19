from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

# 定義使用者資料格式
class User(BaseModel):
    id: str
    name: str
    email: str

# 儲存資料目錄
DATA_DIR = "user_data"
os.makedirs(DATA_DIR, exist_ok=True)

@app.post("/user/add")
def add_user(user: User):
    filename = f"user_{user.id}.json"
    filepath = os.path.join(DATA_DIR, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(user.dict(), f, ensure_ascii=False, indent=2)

    return {"message": f"User {user.id} saved successfully"}

@app.get("/users")
def get_all_users():
    users = []
    for filename in os.listdir(DATA_DIR):
        if filename.startswith("user_") and filename.endswith(".json"):
            filepath = os.path.join(DATA_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    users.append(data)
                except json.JSONDecodeError:
                    continue
    return {"users": users}

@app.get("/user/{user_id}")
def get_user_by_id(user_id: str):
    filename = f"user_{user_id}.json"
    filepath = os.path.join(DATA_DIR, filename)

    if not os.path.isfile(filepath):
        raise HTTPException(status_code=404, detail="User not found")

    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            return data
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Error reading user data")
