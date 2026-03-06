from datetime import datetime
from backend.models.user_model import usage_collection
from backend.config.config import FREE_PLAN_LIMIT, PRO_PLAN_LIMIT


def get_current_month():
    return datetime.utcnow().strftime("%Y-%m")


def get_usage(user_id):
    month = get_current_month()

    usage = usage_collection.find_one({
        "user_id": user_id,
        "month": month
    })

    if not usage:
        usage_collection.insert_one({
            "user_id": user_id,
            "month": month,
            "pr_reviews": 0
        })

        return 0

    return usage["pr_reviews"]


def increment_usage(user_id):
    month = get_current_month()

    usage_collection.update_one(
        {"user_id": user_id, "month": month},
        {"$inc": {"pr_reviews": 1}}
    )


def check_limit(user):
    usage = get_usage(user["user_id"])

    if user["subscription"] == "pro":
        return True

    if usage >= FREE_PLAN_LIMIT:
        return False

    return True