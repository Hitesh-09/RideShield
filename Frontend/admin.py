import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Admin Dashboard", layout="wide")

st.title("🧑‍💼 Admin Dashboard")

# ---------------- FETCH DATA ----------------
users = requests.get(f"{BASE_URL}/user").json()
policies = requests.get(f"{BASE_URL}/policy").json()
claims = requests.get(f"{BASE_URL}/claim").json()

# ---------------- METRICS ----------------
st.subheader("📊 System Overview")

col1, col2, col3 = st.columns(3)

col1.metric("👥 Users", len(users))
col2.metric("📜 Policies", len(policies))
col3.metric("💰 Claims", len(claims))

st.markdown("---")

# ---------------- USERS ----------------
st.subheader("👤 Users")

if users:
    st.dataframe(users)
else:
    st.info("No users found")

st.markdown("---")

# ---------------- POLICIES ----------------
st.subheader("📜 Policies")

if policies:
    st.dataframe(policies)
else:
    st.info("No policies found")

st.markdown("---")

# ---------------- CLAIMS ----------------
st.subheader("💰 Claims")

if claims:
    for claim in claims:
        st.markdown(f"""
        **User ID:** {claim['user_id']}  
        **Event:** {claim['event_type']}  
        **Payout:** ₹{claim['payout_amount']}  
        **Status:** {claim['status']}  
        ---
        """)
else:
    st.info("No claims yet")