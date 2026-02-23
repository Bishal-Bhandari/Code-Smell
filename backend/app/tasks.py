from app.celery_app import celery
from app.github_service import get_pr_files, post_pr_comment
from app.analyzer import analyze_code
from app.llm_service import review_with_llm

@celery.task
def process_pr(owner, repo_name, pr_number):
    """
    Fetches PR files, analyzes them (static + LLM), 
    and posts review comment asynchronously.
    """
    files = get_pr_files(owner, repo_name, pr_number)
    full_review_text = "AI Code Review Report\n\n"

    for file in files:
        static_result = analyze_code(file["code"])
        llm_result = review_with_llm(file["code"])

        full_review_text += f"**{file['filename']}**\n\n"
        full_review_text += f"**Static Analysis:**\n{static_result}\n\n"
        full_review_text += f"**LLM Review:**\n{llm_result}\n\n---\n\n"

    post_pr_comment(owner, repo_name, pr_number, full_review_text)