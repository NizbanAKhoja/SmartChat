from pymongo import MongoClient
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient("mongodb://localhost:27017/")
db = client["llmdb"]
users_collection = db["users"]

def check_user_exists(username, email):
    return users_collection.find_one({"$or": [{"username": username}, {"email": email}]})

def create_user(email, username, password, phone_number):
    hashed_password = generate_password_hash(password)
    api_key = str(uuid.uuid4())
    user_data = {
        "email": email,
        "username": username,
        "password": hashed_password,
        "phone_number": phone_number,
        "api_key": api_key
    }
    users_collection.insert_one(user_data)
    return api_key

def authenticate_user(username, password):
    user = users_collection.find_one({"username": username})
    if user and check_password_hash(user["password"], password):
        return True
    return False
