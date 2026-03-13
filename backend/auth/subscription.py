from fastapi import HTTPException
from backend.auth.models import increment_usage
from backend.config.config import FREE_PLAN_LIMIT, PRO_PLAN_LIMIT

def validate_usage(user):
    if user["subscription"] == "free" and user["usage_count"] >= 10:
        raise HTTPException(status_code=403, 
                            detail="Free plan limit reached")

    increment_usage(user["_id"])

#user plan limits
def get_user_limit(plan: str):
    if plan == "pro":
        return PRO_PLAN_LIMIT
    return FREE_PLAN_LIMIT