from datetime import datetime, timedelta
from fastapi import HTTPException

FREE_LIMIT = 50
PRO_LIMIT = 999999


def check_and_update_usage(user: dict):
    now = datetime.utcnow()

    # reset usage monthly
    if not user.get("usage_reset_date") or user["usage_reset_date"] < now:
        user["usage_count"] = 0
        user["usage_reset_date"] = now + timedelta(days=30)

    # determine limit
    limit = FREE_LIMIT if user["subscription"] == "free" else PRO_LIMIT

    if user["usage_count"] >= limit:
        raise HTTPException(status_code=403, detail="Usage limit exceeded")

    # increase usage count
    user["usage_count"] += 1

    return user