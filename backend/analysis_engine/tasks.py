from backend.celery_apps.celery_app import celery
from backend.github_service.github_service import get_pr_files, post_pr_comment, fetch_pr_files
from backend.analysis_engine.analyzer import analyze_code
from backend.analysis_engine.llm_service import review_with_llm
from backend.db_service.db import pr_collection, db
from backend.db_service.query import increment_usage, save_pr_analysis
from datetime import datetime


@celery.task
def process_pr(user_email, owner, repo_name, pr_number):

    files = get_pr_files(owner, repo_name, pr_number)

    full_review_text = "AI Code Review Report\n\n"
    analysis_results = []

    for file in files:

        static_result = analyze_code(file["code"])

        try:
            llm_result = review_with_llm(file["code"])
        except:
            llm_result = "LLM unavailable. Static analysis only"

        analysis_results.append({
            "filename": file["filename"],
            "static_analysis": static_result,
            "llm_review": llm_result
        })

        full_review_text += f"**{file['filename']}**\n\n"
        full_review_text += f"**Static Analysis:**\n{static_result}\n\n"
        full_review_text += f"**LLM Review:**\n{llm_result}\n\n---\n\n"

    # post comment on github
    post_pr_comment(owner, repo_name, pr_number, full_review_text)

    # save analysis in MongoDB
    pr_collection.insert_one({
        "user_email": user_email,
        "owner": owner,
        "repo": repo_name,
        "pr_number": pr_number,
        "files": analysis_results,
        "review_comment": full_review_text,
        "timestamp": datetime.utcnow()
    })

    # increment usage for subscription tracking
    increment_usage(user_email)

# reset monthly usages count fpr all users
def reset_monthly_usage():
    usage_collection = db["usage"]

    usage_collection.update_many(
        {},
        {"$set": {"count": 0}}
    )

    return {"status": "usage reset"}

# celery beat task to reset usage count
@celery.task
def analyze_pr_task(owner, repo, pr_number):

    files = fetch_pr_files(owner, repo, pr_number)

    results = []

    for file in files:
        analysis = analyze_code(file["patch"])
        results.append({
            "file": file["filename"],
            "analysis": analysis
        })

    save_pr_analysis(owner, repo, pr_number, results)

    return {"status": "done"}