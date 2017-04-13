Python task queue test
======================

Comparing RabbitMQ and AQS SQS with Celery

gateway and worker on separate EC2 instances

code on separate branches, `sqs` and `rabbit`

## rabbit:
- broker must be specified in `app/broker_cred.py` as `URL = 'amqp://user:pass@server:5672//'`