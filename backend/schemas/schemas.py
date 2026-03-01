from pydantic import BaseModel, EmailStr

class CodeRequest(BaseModel):
    code: str

class PRRequest(BaseModel):
    owner: str
    repo: str
    pr_number: int

# signup/login
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserLogin(UserBase):
    email: EmailStr
    password: str

# jwt token
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# subscription
class SubscriptionCheck(BaseModel):
    subscription: str
    usage_count: int