import ast
from radon.complexity import cc_visit
from backend.analysis_engine.llm_service import review_with_llm


def analyze_code(code: str):
    try:
        # static AST parsing
        tree = ast.parse(code)

        # cyclomatic complexity analysis
        complexity = cc_visit(code)

        static_analysis = {
            "functions": [c.name for c in complexity],
            "complexity": [
                {
                    "name": c.name,
                    "score": c.complexity
                }
                for c in complexity
            ]
        }

        # AI code review
        ai_review = review_with_llm(code)

        return {
            "static_analysis": static_analysis,
            "ai_review": ai_review
        }

    except Exception as e:
        return {"error": str(e)}