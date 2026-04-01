from fastapi import FastAPI
from routes import user, policy, claim

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(policy.router, prefix="/policy", tags=["Policy"])
app.include_router(claim.router, prefix="/claim", tags=["Claim"])

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}