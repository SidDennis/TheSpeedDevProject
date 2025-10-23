from pymongo import MongoClient
import redis
from app.config import settings

class Database:
    client: MongoClient = None
    redis_client: redis.Redis = None

db = Database()

def connect_to_mongo():
    """Create database connection"""
    db.client = MongoClient(settings.MONGODB_URL)
    print("Connected to MongoDB")

def close_mongo_connection():
    """Close database connection"""
    if db.client:
        db.client.close()
        print("Disconnected from MongoDB")

def connect_to_redis():
    """Create Redis connection"""
    db.redis_client = redis.from_url(settings.REDIS_URL)
    print("Connected to Redis")

def close_redis_connection():
    """Close Redis connection"""
    if db.redis_client:
        db.redis_client.close()
        print("Disconnected from Redis")

def get_database():
    return db.client[settings.MONGODB_DATABASE]

def get_redis():
    return db.redis_client
