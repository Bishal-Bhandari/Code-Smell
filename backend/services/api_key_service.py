import secrets
from backend.models.api_key_model import api_keys_collection


def generate_api_key(user_id):

    key = secrets.token_hex(32)

    api_keys_collection.insert_one({
        "user_id": user_id,
        "api_key": key
    })

    return key


def validate_api_key(key):

    data = api_keys_collection.find_one({"api_key": key})

    if not data:
        return None

    return data["user_id"]