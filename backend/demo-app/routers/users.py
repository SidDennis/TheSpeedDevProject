from fastapi import APIRouter, HTTPException, Depends
from typing import List
from bson import ObjectId
from app.database import get_database, get_redis
from app.models import User, UserCreate, UserUpdate, UserResponse
from datetime import datetime
import json

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db=Depends(get_database), redis=Depends(get_redis)):
    """Create a new user"""
    # Check if user already exists
    existing_user = db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    
    # Create user document
    user_dict = user.dict()
    user_dict["created_at"] = user_dict["updated_at"] = datetime.utcnow()
    
    result = db.users.insert_one(user_dict)
    created_user = db.users.find_one({"_id": result.inserted_id})
    
    # Cache the user in Redis
    redis.setex(f"user:{result.inserted_id}", 3600, json.dumps(created_user, default=str))
    
    return UserResponse(**created_user, id=str(created_user["_id"]))

@router.get("/", response_model=List[UserResponse])
def get_users(skip: int = 0, limit: int = 10, db=Depends(get_database)):
    """Get all users with pagination"""
    users = []
    for user in db.users.find().skip(skip).limit(limit):
        # Ensure datetime fields are properly handled
        if user.get("created_at") is None:
            user["created_at"] = datetime.utcnow()
        if user.get("updated_at") is None:
            user["updated_at"] = datetime.utcnow()
        users.append(UserResponse(**user, id=str(user["_id"])))
    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db=Depends(get_database), redis=Depends(get_redis)):
    """Get a specific user by ID"""
    # Try to get from cache first
    cached_user = redis.get(f"user:{user_id}")
    if cached_user:
        user_data = json.loads(cached_user)
        return UserResponse(**user_data, id=str(user_data["_id"]))
    
    # If not in cache, get from database
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Cache the user
    redis.setex(f"user:{user_id}", 3600, json.dumps(user, default=str))
    
    return UserResponse(**user, id=str(user["_id"]))

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: str, user_update: UserUpdate, db=Depends(get_database), redis=Depends(get_redis)):
    """Update a user"""
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    # Check if user exists
    existing_user = db.users.find_one({"_id": ObjectId(user_id)})
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Prepare update data
    update_data = {k: v for k, v in user_update.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No data to update")
    
    update_data["updated_at"] = datetime.utcnow()
    
    # Update user
    db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    updated_user = db.users.find_one({"_id": ObjectId(user_id)})
    
    # Update cache
    redis.setex(f"user:{user_id}", 3600, json.dumps(updated_user, default=str))
    
    return UserResponse(**updated_user, id=str(updated_user["_id"]))

@router.delete("/{user_id}")
def delete_user(user_id: str, db=Depends(get_database), redis=Depends(get_redis)):
    """Delete a user"""
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    # Check if user exists
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete user
    db.users.delete_one({"_id": ObjectId(user_id)})
    
    # Remove from cache
    redis.delete(f"user:{user_id}")
    
    return {"message": "User deleted successfully"}
