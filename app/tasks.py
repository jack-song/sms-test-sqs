"""worker module"""
import time

from celery import Celery

import config

# adjust
TASK_DURATION = 0.5

# first argument current module name, broker doesn't need keys if set for boto already
CELERY_APP = Celery('tasks', broker=config.BROKER_URL)

@CELERY_APP.task
def run_test(time_queued):
    """worker job, sleep and record time of completion"""
    # blocks thread (hopefully)
    time.sleep(TASK_DURATION)
    record = 'queued:{} completed:{}\n'.format(time_queued, time.time())
    print(record)
    with open('log.txt', 'a+') as log_file:
        log_file.write(record)
