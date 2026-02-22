from fastapi import FastAPI, Request
from app.schemas import CodeRequest
from app.analyzer import analyze_code
from app.llm_service import review_with_llm
from app.github_service import get_pr_files
from app.schemas import PRRequest

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI Code Reviewer Running"}

@app.post("/analyze")
def analyze(request: CodeRequest):
    static_result = analyze_code(request.code)
    llm_result = review_with_llm(request.code)

    return {
        "static_analysis": static_result,
        "llm_review": llm_result
    }

@app.post("/analyze-pr")
def analyze_pr(request: PRRequest):

    files = get_pr_files(
        request.owner,
        request.repo,
        request.pr_number
    )

    results = []
    full_review_text = "## 🤖 AI Code Review Report\n\n"

    for file in files:
        static_result = analyze_code(file["code"])
        try:
            llm_result = review_with_llm(file["code"])
        except Exception as e:
            llm_result = "LLM unavailable. Static analysis only"

        full_review_text += f"### 📄 {file['filename']}\n\n"
        full_review_text += f"**Static Analysis:**\n{static_result}\n\n"
        full_review_text += f"**LLM Review:**\n{llm_result}\n\n---\n\n"

        results.append({
            "filename": file["filename"],
            "static_analysis": static_result,
            "llm_review": llm_result
        })

    # Post comment to PR
    from app.github_service import post_pr_comment
    post_pr_comment(
        request.owner,
        request.repo,
        request.pr_number,
        full_review_text
    )

    return {
        "message": "Review posted to PR successfully.",
        "total_files": len(results)
    }


@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    # Only pull request
    if payload.get("action") in ["opened", "synchronize"]:
        pr = payload.get("pull_request")
        repo = payload.get("repository")

        owner = repo["owner"]["login"]
        repo_name = repo["name"]
        pr_number = pr["number"]

        files = get_pr_files(owner, repo_name, pr_number)

        full_review_text = "AI Code Review Report\n\n"

        for file in files:
            static_result = analyze_code(file["code"])
            try:
                llm_result = review_with_llm(file["code"])
            except:
                llm_result = "LLM unavailable. Static analysis only"

            full_review_text += f"###{file['filename']}\n\n"
            full_review_text += f"**Static Analysis:**\n{static_result}\n\n"
            full_review_text += f"**LLM Review:**\n{llm_result}\n\n---\n\n"

        from app.github_service import post_pr_comment
        post_pr_comment(owner, repo_name, pr_number, full_review_text)

    return {"status": "Webhook received"}