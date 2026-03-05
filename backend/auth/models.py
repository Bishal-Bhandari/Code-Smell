from backend.db_service.db import db
from datetime import datetime
from bson import ObjectId

def create_user(email: str, hashed_password: str, api_key: str):
    user_data = {
        "email": email,
        "password": hashed_password,  # login verification
        "api_key": api_key,
        "subscription": "free",        # free | pro
        "usage_count": 0,              # monthly usage tracker
        "usage_reset_date": None,      # reset logic handled on first review
        "created_at": datetime.utcnow()
    }

    return db.users.insert_one(user_data)

# GET USER BY EMAIL
def get_user_by_email(email: str):
    return db.users.find_one({"email": email})


# GET USER BY API KEY
def get_user_by_api_key(api_key: str):
    return db.users.find_one({"api_key": api_key})

# UPDATE USER SUBSCRIPTION
def update_subscription(email: str, new_plan: str):
    return db.users.update_one(
        {"email": email},
        {"$set": {"subscription": new_plan}}
    )

# UPDATE USAGE DATA
def update_usage(email: str, usage_count: int, usage_reset_date):
    return db.users.update_one(
        {"email": email},
        {
            "$set": {
                "usage_count": usage_count,
                "usage_reset_date": usage_reset_date
            }
        }
    )