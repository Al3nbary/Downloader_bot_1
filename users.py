import json
from datetime import datetime

FILE = "users.json"

def save_user(user):
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    if user.id not in [u["id"] for u in data["users"]]:
        data["users"].append({
            "id": user.id,
            "username": user.username,
            "name": user.first_name,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)