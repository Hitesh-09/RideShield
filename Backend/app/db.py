import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Debug check (remove later if you want)
if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Missing Supabase environment variables")

# Create client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_policies():
    # fetch only active policies
    return supabase.table("policies").select("*").eq("active", True).execute().data


def create_claim(claim_data):
    return (
        supabase
        .table("claims")
        .insert(claim_data)
        .execute()
    )