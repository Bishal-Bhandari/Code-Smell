from fastapi import Request
from backend.services.api_key_service import validate_api_key


async def api_key_auth(request: Request):

    key = request.headers.get("x-api-key")

    if not key:
        return None

    user_id = validate_api_key(key)

    return user_id