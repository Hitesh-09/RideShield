from fastapi import APIRouter
from app.db import supabase

router = APIRouter()

# Register new user
@router.post("/register")
def register_user(user: dict):
    response = supabase.table("users").insert(user).execute()

    print(response.data)   # ✅ correct place

    return response.data


# Get all users
@router.get("/")
def get_users():
    response = supabase.table("users").select("*").execute()
    return response.data


# Get user by ID
@router.get("/{user_id}")
def get_user(user_id: str):
    response = supabase.table("users").select("*").eq("id", user_id).execute()
    return response.data