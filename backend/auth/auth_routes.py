from fastapi import APIRouter, HTTPException, status
from passlib.context import CryptContext
from backend.schemas.schemas import UserCreate, UserLogin, Token
from backend.auth.models import create_user, get_user_by_email
from backend.auth.dependencies import create_access_token
import secrets

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# signup
@router.post("/signup", response_model=Token)
def signup(user: UserCreate):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = pwd_context.hash(user.password)
    api_key = secrets.token_hex(16)
    create_user(user.email, hashed_password, api_key=api_key)

    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token}

# login
@router.post("/login", response_model=Token)
def login(user: UserLogin):
    db_user = get_user_by_email(user.email)
    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token}