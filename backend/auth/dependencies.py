from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordBearer
from backend.auth.models import get_user_by_email
from backend.config.config import settings
from backend.auth.subscription import get_user_limit
from backend.db_service.query import get_usage_count
from backend.db_service.db import db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise Exception()
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    user = get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


def check_usage(user):

    limit = get_user_limit(user.get("plan", "free"))
    used = get_usage_count(user["email"])

    if used >= limit:
        raise HTTPException(
            status_code=429,
            detail="Usage limit reached. Upgrade plan."
        )
# for verifying api
async def verify_api_key(x_api_key: str = Header(None)):

    if not x_api_key:
        raise HTTPException(status_code=401, detail="API key missing")

    user = db["users"].find_one({"api_key": x_api_key})

    if not user:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return user

# For dashboard endpoints
def get_current_user(token: str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )

        user_id = payload.get("user_id")

        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = db["users"].find_one({"id": user_id})

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")