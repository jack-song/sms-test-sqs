"""worker module"""
import time

from celery import Celery

import broker_cred

# first argument current module name, broker doesn't need keys if set for boto already
CELERY_APP = Celery('tasks', broker=broker_cred.URL)

@CELERY_APP.task
def run_test(message_id):
    """worker job"""
    print(message_id)
    time.sleep(1)
