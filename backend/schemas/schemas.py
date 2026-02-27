from pydantic import BaseModel

class CodeRequest(BaseModel):
    code: str

class PRRequest(BaseModel):
    owner: str
    repo: str
    pr_number: int

# Signup/Login
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    password: str

# JWT token
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Subscription
class SubscriptionCheck(BaseModel):
    subscription: str
    usage_count: int