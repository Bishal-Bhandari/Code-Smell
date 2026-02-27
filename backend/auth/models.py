from db_service.db import db
from datetime import datetime
from bson import ObjectId

users_collection = db["users"]

def create_user(email, password_hash, subscription="free", api_key=None):
    user = {
        "email": email,
        "password": password_hash,
        "subscription": subscription,
        # free / pro / enterprise  
        "api_key": api_key,
        "usage_count": 0,
        "created_at": datetime.utcnow()
    }
    return users_collection.insert_one(user)

def get_user_by_email(email):
    return users_collection.find_one({"email": email})

def increment_usage(user_id):
    users_collection.update_one({"_id": ObjectId(user_id)}, {"$inc": {"usage_count": 1}})