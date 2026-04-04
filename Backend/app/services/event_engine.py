import time
from app.services.weather_service import get_weather, get_aqi
from app.services.claim_service import trigger_claim_for_policy
from app.db import get_policies, supabase

THRESHOLD_RAIN = 80

def run_event_engine():
    print("Running event engine...")

    policies = get_policies()  # fetch active policies

    for policy in policies:
        city = policy["location"]

        weather = get_weather(city)
        rainfall = weather["rainfall"]

        print(f"{city} rainfall: {rainfall}")

        if rainfall > THRESHOLD_RAIN:
            print("Triggering claim...")
            trigger_claim_for_policy(policy, rainfall)

        if weather["aqi"] > 400:
            print("Triggering claim for high AQI...")
            trigger_claim_for_policy(policy, weather["aqi"], "aqi")


def check_events():
    print("Checking events...")

    # Get all users
    users = supabase.table("users").select("*").execute()

    for user in users.data:
        city = user["location"]

        weather = get_weather(city)
        rainfall = weather["rainfall"]
        temp = weather["temperature"]

        # For AQI we need lat/lon (mock for now)
        lat, lon = 19.0760, 72.8777  # Mumbai (can improve later)
        aqi = get_aqi(lat, lon)

        print(f"{city} → Rain: {rainfall}, Temp: {temp}, AQI: {aqi}")

        event_triggered = False
        event_type = ""

        # 🌧 Rain trigger
        if rainfall >= 2:
            event_triggered = True
            event_type = "rain"

        # 🌡 Heatwave trigger
        elif temp >= 40:
            event_triggered = True
            event_type = "heatwave"

        # 🌫 AQI trigger
        elif aqi >= 4:
            event_triggered = True
            event_type = "pollution"

        if event_triggered:

            existing_claim = supabase.table("claims") \
                .select("*") \
                .eq("user_id", user["id"]) \
                .eq("event_type", event_type) \
                .execute()

            if existing_claim.data:
                print(f"{event_type} claim exists → skipping")
                continue

            claim = {
                "user_id": user["id"],
                "event_type": event_type,
                "payout_amount": 400,
                "status": "triggered"
            }

            supabase.table("claims").insert(claim).execute()
            print(f"{event_type} claim created for {city}")
