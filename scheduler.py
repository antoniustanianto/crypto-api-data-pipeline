import schedule
import time
from pipeline import run_pipeline

def job():
    print("Running scheduled pipeline...")
    run_pipeline()

schedule.every(10).minutes.do(job)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)