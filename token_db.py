import time

TOKEN_DB = {}

def activate_token(user_id):
    TOKEN_DB[user_id] = {
        "active": True,
        "expires_at": time.time() + 3600  # 1 hour validity
    }

def is_token_active(user_id):
    data = TOKEN_DB.get(user_id)
    return data and data["active"] and data["expires_at"] > time.time()

def cleanup_expired_tokens():
    now = time.time()
    for user_id in list(TOKEN_DB.keys()):
        if TOKEN_DB[user_id]["expires_at"] <= now:
            TOKEN_DB[user_id]["active"] = False
