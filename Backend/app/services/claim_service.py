from app.db import create_claim, supabase
from datetime import date

def already_claimed_today(policy_id):
    today = str(date.today())

    res = (
        supabase
        .table("claims")
        .select("*")
        .eq("policy_id", policy_id)
        .gte("created_at", today)
        .execute()
    )

    return len(res.data) > 0

def process_payout(user_id, amount):
    print(f"💸 Paying ₹{amount} to user {user_id}")

def trigger_claim_for_policy(policy, event_value, event_type="rain"):
    if already_claimed_today(policy["id"]):
        print("Already claimed today, skipping...")
        return

    claim_data = {
        "user_id": policy["user_id"],
        "policy_id": policy["id"],
        "event_type": event_type,
        "event_value": event_value,
        "status": "triggered"
    }

    create_claim(claim_data)
    process_payout(policy["user_id"], 500)