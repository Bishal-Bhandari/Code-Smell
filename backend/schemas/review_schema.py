from pydantic import BaseModel

class ReviewRequest(BaseModel):
    repo_url: str
    pr_number: int