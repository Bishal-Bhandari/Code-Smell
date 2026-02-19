from fastapi import FastAPI
from app.schemas import CodeRequest
from app.analyzer import analyze_code
from app.llm_service import review_with_llm

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
