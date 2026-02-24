from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

# db name
db = client["ai_code_review_db"]  
# collection name
pr_collection = db["pr_analyses"]  