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