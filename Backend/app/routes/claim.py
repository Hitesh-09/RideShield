from fastapi import APIRouter
from app.db import supabase

router = APIRouter()

# Trigger claim based on event
@router.post("/trigger")
def trigger_claim(event: dict):

    """
    Expected input:
    {
        "user_id": "uuid",
        "type": "rain",
        "value": 120,
        "threshold": 80
    }
    """

    # Check condition
    if event["value"] > event["threshold"]:

        payout = 400  # fixed for now (you can make dynamic later)

        claim_data = {
            "user_id": event["user_id"],
            "event_type": event["type"],
            "payout_amount": payout,
            "status": "triggered"
        }

        response = supabase.table("claims").insert(claim_data).execute()

        return {
            "message": "Claim triggered 🚀",
            "data": response.data
        }

    return {"message": "No claim triggered"}


# Get all claims
@router.get("/")
def get_claims():
    response = supabase.table("claims").select("*").execute()
    return response.data


# Get claims for a user
@router.get("/{user_id}")
def get_user_claims(user_id: str):
    response = supabase.table("claims").select("*").eq("user_id", user_id).execute()
    return response.data