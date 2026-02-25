# backend/main.py
from fastapi import FastAPI, Request
from .analysis_engine.analyzer import analyze_code
from .analysis_engine.llm_service import review_with_llm
from .analysis_engine.tasks import process_pr
from .github_service.github_service import get_pr_files, post_pr_comment
from .schemas.schemas import CodeRequest, PRRequest
from .db_service.query import get_pr_history
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root Endpoint
@app.get("/")
def root():
    return {"status": "AI Code Reviewer Running"}

# Analyze Single Code Snippet
@app.post("/analyze")
def analyze(request: CodeRequest):
    static_result = analyze_code(request.code)
    llm_result = review_with_llm(request.code)

    return {
        "static_analysis": static_result,
        "llm_review": llm_result
    }

# Analyze PR manual call
@app.post("/analyze-pr")
def analyze_pr(request: PRRequest):
    files = get_pr_files(request.owner, request.repo, request.pr_number)
    results = []
    full_review_text = "AI Code Review Report\n\n"

    for file in files:
        static_result = analyze_code(file["code"])
        try:
            llm_result = review_with_llm(file["code"])
        except Exception:
            llm_result = "LLM unavailable. Static analysis only"

        full_review_text += f"{file['filename']}\n\n"
        full_review_text += f"**Static Analysis:**\n{static_result}\n\n"
        full_review_text += f"**LLM Review:**\n{llm_result}\n\n---\n\n"

        results.append({
            "filename": file["filename"],
            "static_analysis": static_result,
            "llm_review": llm_result
        })

    post_pr_comment(request.owner, request.repo, request.pr_number, full_review_text)

    return {
        "message": "Review posted to PR successfully.",
        "total_files": len(results)
    }

# GitHub Webhook Endpoint
@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    if payload.get("action") in ["opened", "synchronize"]:
        pr = payload.get("pull_request")
        repo = payload.get("repository")

        owner = repo["owner"]["login"]
        repo_name = repo["name"]
        pr_number = pr["number"]

        # queue task to celery
        process_pr.delay(owner, repo_name, pr_number)

    return {"status": "Task queued"}

# Dashboard Endpoint 
@app.get("/dashboard/pr-history/{owner}/{repo}")
def dashboard_pr_history(owner: str, repo: str, limit: int = 10):

    results = get_pr_history(owner, repo, limit)
    return {"total": len(results), "prs": results}
