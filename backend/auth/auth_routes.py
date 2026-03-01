from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from schemas.schemas import UserCreate, UserLogin, Token
from auth.models import create_user, get_user_by_email
from auth.dependencies import create_access_token
import secrets

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signup", response_model=Token)
def signup(user: UserCreate):

    existing = get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = pwd_context.hash(user.password)
    api_key = secrets.token_hex(16)

    create_user(user.email, hashed_password, api_key)

    token = create_access_token({"sub": user.email})
    return {"access_token": token}

@router.post("/login", response_model=Token)
def login(user: UserLogin):

    db_user = get_user_by_email(user.email)
    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token}