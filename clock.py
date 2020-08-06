from datetime import datetime
from server import sendback
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sendback, 'interval', minutes=5)

sched.start()