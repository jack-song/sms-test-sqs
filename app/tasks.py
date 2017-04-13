"""worker module"""
import time

from celery import Celery

# adjust
TASK_DURATION = 1.2

options= {
    # downtime only if queue is empty (busy default)
    'polling_interval': .3,
    # can be set here or on AWS console
    'wait_time_seconds': 20
}

# first argument current module name, broker doesn't need keys if set for boto already
CELERY_APP = Celery('tasks', broker='sqs://', broker_transport_options = options)

@CELERY_APP.task
def run_test(time_queued):
    """worker job, sleep and record time of completion"""
    # blocks thread (hopefully)
    time.sleep(TASK_DURATION)
    record = 'queued:{} completed:{}\n'.format(time_queued, time.time())
    print(record)
    with open('log.txt', 'a+') as log_file:
        log_file.write(record)
