from db_service.db import db
from datetime import datetime
from bson import ObjectId

users_collection = db["users"]

def create_user(email, password_hash, subscription="free", api_key=None):
    user = {
        "email": email,
        "password": password_hash,
        # free / pro / enterprise
        "subscription": subscription,  
        "api_key": api_key,
        "usage_count": 0,
        "created_at": datetime.utcnow()
    }