import time
import threading

from fastapi import FastAPI
from Backend.app.routes import claim, policy
from app.routes import user
from app.services.event_engine import check_events

app = FastAPI()

@app.on_event("startup")
def start_event_engine():
    thread = threading.Thread(target=run_event_engine)
    thread.daemon = True
    thread.start()


def run_event_engine():
    while True:
        check_events()
        time.sleep(120)  # every 2 min

app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(policy.router, prefix="/policy", tags=["Policy"])
app.include_router(claim.router, prefix="/claim", tags=["Claim"])

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}