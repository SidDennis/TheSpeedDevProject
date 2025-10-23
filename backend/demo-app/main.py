from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import connect_to_mongo, close_mongo_connection, connect_to_redis, close_redis_connection
from app.routers import users

app = FastAPI(
    title="TheSpeedDevProject API",
    description="A FastAPI backend with MongoDB and Redis",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix="/api/v1")

@app.on_event("startup")
def startup_event():
    connect_to_mongo()
    connect_to_redis()

@app.on_event("shutdown")
def shutdown_event():
    close_mongo_connection()
    close_redis_connection()

@app.get("/")
def root():
    return {"message": "Welcome to TheSpeedDevProject API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}