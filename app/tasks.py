import time

from celery import Celery

import broker_cred

# first argument current module name, broker doesn't need keys if set for boto already
app = Celery('tasks', broker=broker_cred.URL)

@app.task
def run_test(message_id):
    print(message_id)
    time.sleep(1)
