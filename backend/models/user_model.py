from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["ai_code_review_db"]

usage_collection = db["usage"]