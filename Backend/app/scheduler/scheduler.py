from apscheduler.schedulers.background import BackgroundScheduler
from app.services.event_engine import run_event_engine

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.add_job(run_event_engine, "interval", minutes=5)
    scheduler.start()