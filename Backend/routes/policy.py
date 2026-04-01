from fastapi import APIRouter
from db import supabase

router = APIRouter()

# Create policy
@router.post("/create")
def create_policy(policy: dict):
    response = supabase.table("policies").insert(policy).execute()
    return response.data


# Get policies for a user
@router.get("/{user_id}")
def get_user_policies(user_id: str):
    response = supabase.table("policies").select("*").eq("user_id", user_id).execute()
    return response.data


# Get all policies
@router.get("/")
def get_all_policies():
    response = supabase.table("policies").select("*").execute()
    return response.data