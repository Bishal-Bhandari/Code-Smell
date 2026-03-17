import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
 
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    JWT_SECRET = os.getenv("JWT_SECRET", "supersecret")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRE_MINUTES = 60

    FREE_TIER_LIMIT = 50
    PRO_TIER_LIMIT = 500
    ENTERPRISE_LIMIT = 5000

settings = Settings()