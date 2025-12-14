from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserLogin

router = APIRouter(prefix="/api/auth", tags=["Auth"])

# Temporary in-memory database
users_db = []

# Register user
@router.post("/register")
def register_user(user: UserCreate):
    # Check if username already exists
    for u in users_db:
        if u["username"] == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")
    # Add new user
    users_db.append({"username": user.username, "password": user.password})
    return {"message": "User registered successfully"}

# Login user
@router.post("/login")
def login_user(user: UserLogin):
    for u in users_db:
        if u["username"] == user.username and u["password"] == user.password:
            return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid username or password")
