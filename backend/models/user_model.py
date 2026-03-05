from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    hashed_password: str
    # free or pro
    subscription: str = "free"   
    usage_count: int = 0
    usage_reset_date: Optional[datetime] = None
    api_key: Optional[str] = None