# token_db.py

import time
from collections import defaultdict

# Stores: user_id -> { "token": token, "expiry": expiry_timestamp }
token_data = defaultdict(dict)

def generate_token(user_id):
    token = f"TOKEN_{user_id}_{int(time.time())}"
    expiry = time.time() + 3600  # 1 hour validity
    token_data[user_id] = {"token": token, "expiry": expiry}
    return token

def is_token_valid(user_id):
    if user_id in token_data:
        if time.time() < token_data[user_id]["expiry"]:
            return True
    return False

def delete_token(user_id):
    if user_id in token_data:
        del token_data[user_id]
