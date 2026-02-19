import ast
from radon.complexity import cc_visit

def analyze_code(code: str):
    try:
        tree = ast.parse(code)
        complexity = cc_visit(code)

        return {
            "functions": [c.name for c in complexity],
            "complexity": [
                {"name": c.name, "score": c.complexity}
                for c in complexity
            ]
        }

    except Exception as e:
        return {"error": str(e)}
