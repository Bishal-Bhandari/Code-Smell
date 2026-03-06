from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["ai_code_review_db"]

api_keys_collection = db["api_keys"]