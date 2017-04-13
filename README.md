Python task queue test
======================

Comparing RabbitMQ and AQS SQS with Celery

gateway and worker on separate EC2 instances

code on separate branches, `sqs` and `rabbit`

python3, uses flask, celery, boto(for celery+sqs), requests(for profiling only)

## setup

### SQS
- checkout branch `sqs`
- access to SQS must be given to WHOIAM on the gateway and worker instances
- long polling should be used, or comparison may obviously be quite one-sided

### RabbitMQ
- checkout branch `rabbit`
- RabbitMQ must be installed on separate instance
- broker must be specified in `app/config.py` like `app/sample_config.py`

## profiling

### client burden
- gateway url to add a job must be specified in `config.py` like `sample_config.py`
- total processing time, for 1000 jobs is given in seconds

### processing speed
- `app/log.txt` will have stamps for job completion time
- any `n` entries can be inspected to find time elapsed to complete `n` jobs

### cost
- AWS logs and records should be inspected to estimate costs