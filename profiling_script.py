"""run-only script from profiling job processing in queues"""
import requests

import config

total_seconds = 0.0

# http://docs.python-requests.org/en/latest/api/?highlight=elapsed#requests.Response.elapsed
# good for serverside profiling, ignores client side response parsing
for attempt in range(1000):
    seconds_elapsed = requests.get(config.GATEWAY_URL).elapsed.total_seconds()
    total_seconds += seconds_elapsed
    # IO may take up too much time
    # print(seconds_elapsed)
    # with open('log.txt', 'a+') as log_file:
    #     log_file.write('{}\n'.format(seconds_elapsed))

print('total time consumed in seconds for 1000 requests: {}'.format(total_seconds))
