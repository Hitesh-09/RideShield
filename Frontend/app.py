import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Sujeet Protect", layout="centered")

# SESSION STATE
if "user_id" not in st.session_state:
    st.session_state.user_id = None

# ---------------- LOGIN ----------------
if not st.session_state.user_id:
    st.title("📱 Sujeet Protect")
    st.subheader("Insurance for Delivery Workers")

    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    location = st.text_input("City")

    if st.button("Login / Register"):
        res = requests.post(f"{BASE_URL}/user/register", json={
            "name": name,
            "email": email,
            "platform": "swiggy",
            "location": location
        })

        if res.status_code == 200:
            user = res.json()[0]
            st.session_state.user_id = user["id"]
            st.success("Welcome! You're protected now 🚀")

# ---------------- DASHBOARD ----------------
else:
    st.title("📊 Your Protection Dashboard")

    # CREATE POLICY (auto)
    policy_res = requests.post(f"{BASE_URL}/policy/create", json={
        "user_id": st.session_state.user_id
    })

    if policy_res.status_code == 200:
        policy = policy_res.json()[0]

        st.markdown("### 📜 Your Policy")

        col1, col2 = st.columns(2)

        col1.metric("💰 Premium", f"₹{policy['premium']}/week")
        col2.metric("⚠️ Risk Level", policy["risk_level"])

        st.metric("📅 Daily Protection", f"₹{policy['coverage_per_day']}")

    st.markdown("---")

    # CLAIMS
    st.markdown("### 💰 Your Earnings Protection")

    claims_res = requests.get(f"{BASE_URL}/claim")

    if claims_res.status_code == 200:
        claims = claims_res.json()

        user_claims = [c for c in claims if c["user_id"] == st.session_state.user_id]

        if user_claims:
            for claim in user_claims:
                st.success(f"{claim['event_type'].upper()} detected → ₹{claim['payout_amount']} credited")
        else:
            st.info("No disruptions yet. You're covered!")

    st.markdown("---")

    if st.button("Logout"):
        st.session_state.user_id = None