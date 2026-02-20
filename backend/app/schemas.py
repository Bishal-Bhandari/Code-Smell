from pydantic import BaseModel

class CodeRequest(BaseModel):
    code: str

class PRRequest(BaseModel):
    owner: str
    repo: str
    pr_number: int