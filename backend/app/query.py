from app.db import pr_collection

def get_pr_history(owner: str, repo: str, limit: int = 10):
    
    results = pr_collection.find(
        {"owner": owner, "repo": repo}
    ).sort("timestamp", -1).limit(limit)

    return list(results)