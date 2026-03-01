import os
from dotenv import load_dotenv

load_dotenv()

# for mongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# for jwt
JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_MINUTES = 60