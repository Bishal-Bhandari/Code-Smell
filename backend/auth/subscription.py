from backend.db_service.db import db
from backend.config.config import settings


def get_user_usage(user_id):

    collection = db["pr_analyses"]

    return collection.count_documents({"user_id": user_id})


def check_usage_limit(user):

    usage = get_user_usage(user["id"])

    if user["subscription"] == "free":
        limit = settings.FREE_TIER_LIMIT

    elif user["subscription"] == "pro":
        limit = settings.PRO_TIER_LIMIT

    else:
        limit = settings.ENTERPRISE_LIMIT

    if usage >= limit:
        raise Exception("Usage limit exceeded")

    return True

def get_user_limit(plan: str):
    if plan == "free":
        return settings.FREE_TIER_LIMIT
    elif plan == "pro":
        return settings.PRO_TIER_LIMIT
    else:
        return settings.ENTERPRISE_LIMIT