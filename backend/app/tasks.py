from app.celery_app import celery
from app.github_service import get_pr_files, post_pr_comment
from app.analyzer import analyze_code
from app.llm_service import review_with_llm
from app.db import pr_collection
from datetime import datetime

@celery.task
def process_pr(owner, repo_name, pr_number):
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

    # save to MongoDB
    pr_collection.insert_one({
        "owner": owner,
        "repo": repo_name,
        "pr_number": pr_number,
        "files": analysis_results,
        "review_comment": full_review_text,
        "timestamp": datetime.utcnow()
    })