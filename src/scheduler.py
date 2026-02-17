import os
import time
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print(f"Tick! The time is: {datetime.now()}")


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, "interval", seconds=3)
    scheduler.start()
    print("Press Ctrl+{} to exit".format("Break" if os.name == "nt" else "C"))

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
