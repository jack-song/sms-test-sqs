import time

from celery import Celery

options= {'polling_interval': 10}

# first argument current module name, broker doesn't need keys if set for boto already
app = Celery('tasks', broker='sqs://', broker_transport_options=options)

@app.task
def run_test(message_id):
    print(message_id)
    time.sleep(1)
