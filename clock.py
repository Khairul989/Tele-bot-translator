from datetime import datetime
import server
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(server, 'interval', minutes=5)

sched.start()