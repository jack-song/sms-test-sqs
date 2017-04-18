Python task queue test
======================

Comparing RabbitMQ and AQS SQS with Celery

gateway and worker on separate EC2 instances

code on separate branches, `sqs` and `rabbit`

python3, uses flask, celery, boto(for celery+sqs), requests(for profiling only)

## setup

#### SQS
- checkout branch `sqs`
- access to SQS must be given to WHOIAM on the gateway and worker instances
- long polling should be used, or comparison may obviously be quite one-sided

#### RabbitMQ
- checkout branch `rabbit`
- RabbitMQ must be installed on separate instance
- broker must be specified in `app/config.py` like `app/sample_config.py`

## profiling
- adjust job duration
    - longer = lower sensitivity due to sleep dominating measurements
    - shorter = lower sensitivity due to network speed dominating measurements
    - sleep should be fairly accurate, and within-aws speeds should be fast
    - therefore doesn't matter much, but must make guarantee:
    - jobs must run slow enough for there always to be another job in the queue
    - AKA queued messages should always be above 0 throughout run
    - otherwise we're measuring waiting time
- adjust # of jobs
    - more = better precision (repeatable numbers, more confidence in results)
    - less = longer to run
- prefer longer job duration and more jobs
- run times become a significant concern from nairobi

#### client burden
- gateway url to add a job must be specified in `config.py` like `sample_config.py`
- total processing time, for 1000 jobs is given in seconds

#### processing speed
- `app/log.txt` will have stamps for job completion time
- any `n` entries can be inspected to find time elapsed to complete `n` jobs

#### cost
- AWS logs and records should be inspected to estimate costs

## results

#### test run
us-east-1, ec2, t2.micro, .1 second jobs, 100 requests, from nairobi
- 15:55 Nairobi time
- total time consumed in seconds for 100 requests: 59.70401500000001
- line 1: 1492088172.98
- line 100: 1492088232.27
- time to process: 59.2899999619
- apparently google's bad with floating point
- .1 second jobs are too short (fairly meaningless?)
    - confirmed with another run (time to process ~63s, time to request ~65s)

### Set 1
us-east-1, ec2, t2.micro, 1.2 second jobs, 300 requests, from nairobi

#### RabbitMQ

Apr 13, 5pm
- run-1 requesting: 198.38498800000016
- run-1 processing: 360.809999943
- run-2 requesting: 176.98746099999985
- run-2 processing: 359.610000134
- run-3 requesting: 197.1018840000002
- run-3 processing: 359.610000134

Apr 18, 11am
- run-4 requesting: 251.19186099999996
- run-4 processing: 366.289999962
- run-5 requesting: 220.46736300000023
- run-5 processing: 359.639999866

#### AWS SQS

Apr 13, 6pm
- run-1 requesting: 341.88851900000014
- run-1 processing: 378.99000001
- run-2 requesting: 194.95904800000008
- run-2 processing: 365.640000105

Apr 18, 10am
- run-3 requesting: 257.1152150000001
- run-3 processing: 365.75999999
- run-4 requesting: 212.9646309999999
- run-4 processing: 365.109999895
- run-5 requesting: 232.94280699999996
- run-5 processing: 365.450000048