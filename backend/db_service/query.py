from backend.db_service.db import pr_collection
from bson import ObjectId
from datetime import datetime
from backend.db_service.db import db

def serialize_pr(pr_doc):
    return {
        "id": str(pr_doc["_id"]),
        "owner": pr_doc["owner"],
        "repo": pr_doc["repo"],
        "pr_number": pr_doc["pr_number"],
        "files": pr_doc["files"],
        "review_comment": pr_doc["review_comment"],
        "timestamp": pr_doc["timestamp"].isoformat() if isinstance(pr_doc["timestamp"], datetime) else pr_doc["timestamp"]
    }

def get_pr_history(owner: str, repo: str, limit: int = 10):
    results = pr_collection.find(
        {"owner": owner, "repo": repo}
    ).sort("timestamp", -1).limit(limit)

    return [serialize_pr(pr) for pr in results]


def get_pr_history_for_user(email):
    pr_collection = db["pr_analyses"]
    return list(pr_collection.find({"owner": email}))

# Usage tracking functions 
def get_usage_count(user_email):
    collection = db["usage"]
    usage = collection.find_one({"email": user_email})

    if not usage:
        return 0

    return usage["count"]


def increment_usage(user_email):
    collection = db["usage"]

    collection.update_one(
        {"email": user_email},
        {"$inc": {"count": 1}},
        upsert=True
    )