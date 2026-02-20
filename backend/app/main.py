from fastapi import FastAPI
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

    for file in files:
        static_result = analyze_code(file["code"])
        llm_result = review_with_llm(file["code"])

        results.append({
            "filename": file["filename"],
            "static_analysis": static_result,
            "llm_review": llm_result
        })

    return {
        "total_files": len(results),
        "results": results
    }


