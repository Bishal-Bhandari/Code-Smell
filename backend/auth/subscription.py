from fastapi import HTTPException
from backend.auth.models import increment_usage

def validate_usage(user):
    if user["subscription"] == "free" and user["usage_count"] >= 10:
        raise HTTPException(status_code=403, 
                            detail="Free plan limit reached")

    increment_usage(user["_id"])