from fastapi import HTTPException, status
from auth.models import increment_usage

def validate_usage(user):
    # free plan max 3 pull request per day
    if user["subscription"] == "free" and user.get("usage_count", 0) >= 3:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Free plan limit reached. Upgrade to continue."
        )
    # Increment usage
    increment_usage(user["_id"])